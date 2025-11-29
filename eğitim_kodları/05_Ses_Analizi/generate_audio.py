import numpy as np
import soundfile as sf
import os

# Generate 5 seconds of audio
sr = 16000
t = np.linspace(0, 5, sr * 5)
# Mix of sine waves
y = 0.5 * np.sin(2 * np.pi * 440 * t) + 0.3 * np.sin(2 * np.pi * 880 * t) + 0.1 * np.random.normal(0, 1, len(t))

output_path = "../veriler/ornek_ses.wav"
sf.write(output_path, y, sr)
print(f"Created {output_path}")
