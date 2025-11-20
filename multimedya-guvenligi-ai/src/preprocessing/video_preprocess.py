import os
from typing import Optional

import cv2


def extract_frames(
    video_path: str,
    output_dir: str,
    every_n_frames: int = 5,
    resize_to: Optional[tuple[int, int]] = (224, 224),
) -> None:
    """
    Bir video dosyasından periyodik olarak frame çıkarır ve diske kaydeder.

    Parametreler:
        video_path: Girdi video dosyasının yolu.
        output_dir: Çıkarılan frame'lerin kaydedileceği klasör.
        every_n_frames: Kaç frame'de bir görüntü alınacağı.
        resize_to: (width, height) formatında yeniden boyutlandırma değeri.
    """
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    frame_idx = 0
    saved_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % every_n_frames == 0:
            if resize_to is not None:
                frame = cv2.resize(frame, resize_to)
            out_path = os.path.join(output_dir, f"frame_{saved_idx:06d}.jpg")
            cv2.imwrite(out_path, frame)
            saved_idx += 1

        frame_idx += 1

    cap.release()
