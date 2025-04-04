from bark import generate_audio, preload_models
import numpy as np
import scipy.io.wavfile as wav

def text_to_speech(text, output_audio="narration.wav"):
    try:
        preload_models()
        audio_array = generate_audio(text)
        wav.write(output_audio, 24000, np.array(audio_array * 32767, dtype=np.int16))
        print(f"✅ Narration saved as {output_audio}")
    except Exception as e:
        print(f"Error during audio generation: {e}")


if __name__ == "__main__":
    with open("summary.txt", "r", encoding="utf-8") as f:
        text = f.read()

    if text:
        text_to_speech(text)
    else:
        print("❌ No text provided for narration.")
