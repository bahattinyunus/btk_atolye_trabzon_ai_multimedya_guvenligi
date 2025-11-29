# Yüksek Çözünürlüklü Neural Style Transfer (1024px)

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision.models as models

from PIL import Image
import matplotlib.pyplot as plt
import copy
import os

# ----------------------- AYARLAR ----------------------- #
CONTENT_IMAGE_PATH = "../veriler/ai_content.png"
STYLE_IMAGE_PATH   = "../veriler/ai_style.png"
OUTPUT_IMAGE_PATH  = "../veriler/output_hd.jpg"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

IMSIZE = 1024     # 🔥 yüksek çözünürlük
NUM_STEPS = 400   # 🔥 daha kaliteli sonuç
STYLE_WEIGHT = 5e6
CONTENT_WEIGHT = 1.0
# ------------------------------------------------------ #

def load_image(path, imsize=IMSIZE):
    image = Image.open(path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((imsize, imsize)),
        transforms.ToTensor()
    ])
    image = transform(image).unsqueeze(0)
    return image.to(device, torch.float)

def to_image(tensor):
    image = tensor.cpu().clone().detach().squeeze(0)
    return transforms.ToPILImage()(image)

class Normalization(nn.Module):
    def __init__(self, mean, std):
        super().__init__()
        self.mean = torch.tensor(mean).view(-1,1,1).to(device)
        self.std = torch.tensor(std).view(-1,1,1).to(device)
    def forward(self, x):
        return (x - self.mean) / self.std

class ContentLoss(nn.Module):
    def __init__(self, target):
        super().__init__()
        self.target = target.detach()
        self.loss = 0
    def forward(self, input):
        self.loss = F.mse_loss(input, self.target)
        return input

def gram_matrix(x):
    b,c,h,w = x.size()
    features = x.view(b*c, h*w)
    G = torch.mm(features, features.t())
    return G.div(b*c*h*w)

class StyleLoss(nn.Module):
    def __init__(self, target_feature):
        super().__init__()
        self.target = gram_matrix(target_feature).detach()
        self.loss = 0
    def forward(self, input):
        G = gram_matrix(input)
        self.loss = F.mse_loss(G, self.target)
        return input

def build_model(cnn, norm_mean, norm_std, style_img, content_img):
    cnn = copy.deepcopy(cnn)

    normalization = Normalization(norm_mean, norm_std)

    content_losses = []
    style_losses = []

    model = nn.Sequential(normalization)

    i = 0
    for layer in cnn.children():
        if isinstance(layer, nn.Conv2d):
            i += 1
            name = f"conv_{i}"
        elif isinstance(layer, nn.ReLU):
            name = f"relu_{i}"
            layer = nn.ReLU(inplace=False)
        elif isinstance(layer, nn.MaxPool2d):
            name = f"pool_{i}"
        else:
            name = f"layer_{i}"

        model.add_module(name, layer)

        if name == "conv_4":
            target = model(content_img).detach()
            c_loss = ContentLoss(target)
            model.add_module("content_loss", c_loss)
            content_losses.append(c_loss)

        if name in ["conv_1", "conv_2", "conv_3", "conv_4", "conv_5"]:
            target_feature = model(style_img).detach()
            s_loss = StyleLoss(target_feature)
            model.add_module(f"style_loss_{i}", s_loss)
            style_losses.append(s_loss)

    # Gereksiz son katmanları at
    for i in range(len(model)-1, -1, -1):
        if isinstance(model[i], ContentLoss) or isinstance(model[i], StyleLoss):
            break
    model = model[:i+1]

    return model, style_losses, content_losses

def run_style_transfer(cnn, norm_mean, norm_std,
                       content_img, style_img, input_img):

    model, style_losses, content_losses = build_model(
        cnn, norm_mean, norm_std, style_img, content_img
    )

    input_img = input_img.clone()
    input_img.requires_grad_(True)

    optimizer = torch.optim.LBFGS([input_img])

    print("HD Stil aktarımı başlıyor...")

    run = [0]
    while run[0] <= NUM_STEPS:

        def closure():
            with torch.no_grad():
                input_img.clamp_(0, 1)

            optimizer.zero_grad()
            model(input_img)

            style_score = sum(sl.loss for sl in style_losses) * STYLE_WEIGHT
            content_score = sum(cl.loss for cl in content_losses) * CONTENT_WEIGHT

            loss = style_score + content_score
            loss.backward()

            if run[0] % 30 == 0:
                print(f"[{run[0]}/{NUM_STEPS}] Style={style_score:.3f} Content={content_score:.3f}")

            run[0] += 1
            return loss

        optimizer.step(closure)

    with torch.no_grad():
        input_img.clamp_(0,1)

    return input_img


def main():
    content_img = load_image(CONTENT_IMAGE_PATH)
    style_img   = load_image(STYLE_IMAGE_PATH)

    cnn = models.vgg19(weights=models.VGG19_Weights.IMAGENET1K_V1).features.to(device).eval()

    norm_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
    norm_std  = torch.tensor([0.229, 0.224, 0.225]).to(device)

    input_img = content_img.clone()

    output = run_style_transfer(
        cnn, norm_mean, norm_std,
        content_img, style_img, input_img
    )

    out_img = to_image(output)
    out_img.save(OUTPUT_IMAGE_PATH)

    print(f"HD Çıktı kaydedildi → {OUTPUT_IMAGE_PATH}")

    plt.imshow(out_img)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
