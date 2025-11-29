import os                          # Dosya ve klasör işlemleri için gerekli kütüphane
import numpy as np                 # Sayısal işlemler için kullanılan temel bilimsel kütüphane
import librosa                     # Ses sinyallerini işlemek için ana kütüphane
import librosa.display             # Spektrogramların görselleştirilmesi için gerekli
import matplotlib.pyplot as plt    # Grafik ve görüntü çizimi için kullanılan kütüphane


# ---------------------------------------------------------
# 1) Ses yükleme fonksiyonu
# ---------------------------------------------------------
def load_audio(audio_path, target_sr=16000):
    """
    Ses dosyasını yükler, mono hâline getirir ve gerekirse yeniden örnekler.
    """

    y, sr = librosa.load(audio_path, sr=None, mono=True)
    # ↑ Ses dosyasını okur.
    #   sr=None → mevcut örnekleme frekansını koru.
    #   mono=True → stereo ise tek kanala indir.

    if sr != target_sr:
        y = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
        # ↑ Eğer örnekleme frekansı hedef sample rate değilse yeniden örnekle.
        sr = target_sr
        # ↑ Yeni örnekleme frekansını güncelle.

    return y, sr
    # ↑ Yüklenmiş ve yeniden örneklenmiş sesi ve sample rate'i döndür.


# ---------------------------------------------------------
# 2) STFT tabanlı spektrogram kaydetme
# ---------------------------------------------------------
def save_spectrogram(y, sr, out_path,
                     n_fft=2048,
                     hop_length=512,
                     win_length=None,
                     cmap="magma"):
    """
    STFT log-amplitude spektrogramını oluşturup PNG olarak kaydeder.
    """

    stft = librosa.stft(y,
                        n_fft=n_fft,
                        hop_length=hop_length,
                        win_length=win_length)
    # ↑ Short-Time Fourier Transform (STFT) uygular.
    #   n_fft → FFT pencere boyutu
    #   hop_length → adım boyutu (frame kayma miktarı)
    #   win_length → pencere uzunluğu (None → n_fft ile aynı)

    S = np.abs(stft)
    # ↑ STFT kompleks çıktısını mutlak değer alarak magnitüd spektrogramına dönüştür.

    S_db = librosa.amplitude_to_db(S, ref=np.max)
    # ↑ Magnitüdü logaritmik (dB) ölçeğe çevir. İnsan algısına daha yakın.

    plt.figure(figsize=(10, 4))
    # ↑ Yeni bir çizim alanı oluştur (10x4 boyutunda).

    librosa.display.specshow(
        S_db, sr=sr, hop_length=hop_length,
        x_axis="time", y_axis="log",
        cmap=cmap
    )
    # ↑ Spektrogramı zamana karşı log-frekans ölçeğinde çiz.

    plt.colorbar(format="%+2.0f dB")
    # ↑ Sağ tarafa renk ölçeği ekle.

    plt.title("STFT Spectrogram")
    # ↑ Görsel başlığı.

    plt.tight_layout()
    # ↑ Çizim alanını sıkıştır, taşmaları engelle.

    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    # ↑ Spektrogram görüntüsünü dosyaya kaydet (300 DPI kaliteli çıktı).

    plt.close()
    # ↑ Hafıza tüketimini azaltmak için figürü kapat.


# ---------------------------------------------------------
# 3) Mel-tabanlı Cochleagram (yaklaşık) kaydetme
# ---------------------------------------------------------
def save_cochleagram_like(y, sr, out_path,
                          n_mels=128,
                          n_fft=2048,
                          hop_length=512,
                          fmin=50.0,
                          fmax=None,
                          cmap="magma"):
    """
    Mel filtrebank tabanlı Cochleagram-benzeri görüntü oluşturur ve kaydeder.
    """

    if fmax is None:
        fmax = sr / 2
        # ↑ Eğer üst frekans sınırı belirtilmemişse Nyquist frekansı kullanılır.

    mel_spec = librosa.feature.melspectrogram(
        y=y, sr=sr,
        n_fft=n_fft,
        hop_length=hop_length,
        n_mels=n_mels,
        fmin=fmin, fmax=fmax,
        power=2.0
    )
    # ↑ Mel-spektrogram üretir.
    #   n_mels → kaç adet mel filtresi kullanılacağı
    #   power=2 → enerji tabanlı mel hesaplaması (cochleagram'a daha yakın)

    mel_db = librosa.power_to_db(mel_spec, ref=np.max)
    # ↑ Mel spektrogramı dB ölçeğine çevir.

    plt.figure(figsize=(10, 4))
    # ↑ Çizim alanı oluştur.

    librosa.display.specshow(
        mel_db,
        sr=sr,
        hop_length=hop_length,
        x_axis="time",
        y_axis="mel",
        cmap=cmap,
        fmin=fmin, fmax=fmax
    )
    # ↑ Mel-cochleagram görselini zaman-mel ölçeğinde çiz.

    plt.colorbar(format="%+2.0f dB")
    # ↑ Sağ tarafa renk barı ekle.

    plt.title("Mel-based Cochleagram (Approx.)")
    # ↑ Başlık.

    plt.tight_layout()
    # ↑ Sıkı yerleşim.

    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    # ↑ Cochleagram görüntüsünü kaydet.

    plt.close()
    # ↑ Çizimi kapat.


# ---------------------------------------------------------
# 4) Tüm iş akışını yöneten fonksiyon
# ---------------------------------------------------------
def run_pipeline(audio_path,
                 output_dir="outputs",
                 target_sr=16000,
                 n_fft=2048,
                 hop_length=512,
                 n_mels=128):
    """
    Ses → spektrogram → cochleagram üretim süreçlerini sırayla çalıştırır.
    """

    os.makedirs(output_dir, exist_ok=True)
    # ↑ Çıktı klasörü yoksa oluştur.

    print(f"[INFO] Ses yükleniyor: {audio_path}")
    # ↑ Kullanıcıya bilgi mesajı.

    y, sr = load_audio(audio_path, target_sr=target_sr)
    # ↑ Ses yükleme ve yeniden örnekleme

    print(f"[INFO] Ses uzunluğu: {len(y)/sr:.2f} sn, SR: {sr}")
    # ↑ Sesin uzunluğunu saniye cinsinden yazdır.

    spec_path = os.path.join(output_dir, "spectrogram_stft.png")
    # ↑ Spektrogram kaydedilecek yol

    coch_path = os.path.join(output_dir, "cochleagram_mel.png")
    # ↑ Cochleagram kaydedilecek yol

    print(f"[INFO] STFT spektrogram -> {spec_path}")
    # ↑ Bilgi mesajı

    save_spectrogram(
        y, sr, spec_path,
        n_fft=n_fft,
        hop_length=hop_length
    )
    # ↑ STFT spektrogram üret ve kaydet

    print(f"[INFO] Cochleagram (mel) -> {coch_path}")
    # ↑ Bilgi mesajı

    save_cochleagram_like(
        y, sr, coch_path,
        n_fft=n_fft,
        hop_length=hop_length,
        n_mels=n_mels
    )
    # ↑ Cochleagram üret ve kaydet

    print("[INFO] İşlem tamamlandı!")
    # ↑ Son mesaj


# ---------------------------------------------------------
# 5) Parametreleri buradan değiştirip doğrudan çalıştırırsın
# ---------------------------------------------------------
if __name__ == "__main__":

    AUDIO_PATH = "data_ses/ornek.wav"     # ← İşlenecek ses dosyan
    OUT_DIR    = "data_ses"      # ← Çıktı klasörü
    TARGET_SR  = 16000           # ← Yeniden örnekleme frekansı
    N_FFT      = 2048            # ← STFT pencere boyutu
    HOP        = 512             # ← Frame kayması
    N_MELS     = 128             # ← Mel filtre sayısı

    run_pipeline(
        audio_path=AUDIO_PATH,
        output_dir=OUT_DIR,
        target_sr=TARGET_SR,
        n_fft=N_FFT,
        hop_length=HOP,
        n_mels=N_MELS
    )
    # ↑ Tüm iş hattını çalıştır
