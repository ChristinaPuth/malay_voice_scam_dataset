import os
import pandas as pd
from tqdm import tqdm

from utils.ai_generator import generate_sms_samples
from utils.translator import get_translator, translate_texts
from utils.tts import text_to_wav

os.makedirs("data/audio", exist_ok=True)

def is_valid_translation(en, ms):
    """Judge whether the translation quality is qualified"""
    if not en.strip():
        return False
    if ms.strip().lower() in ["", "mengenai", "tentang", "none"]:
        return False
    if len(ms.strip()) < 5:
        return False
    return True

def main():
    num_samples = 10500
    scam_ratio = 0.5

    # Loading existing transcripts
    if os.path.exists("data/transcripts.csv"):
        existing_df = pd.read_csv("data/transcripts.csv")
        records = existing_df.to_dict("records")
    else:
        records = []

    translator = get_translator()

    print(" Starting to generate data...")

    with tqdm(total=num_samples, initial=len(records), desc=" Generation progress", ncols=100) as pbar:
        while len(records) < num_samples:
            english_samples = generate_sms_samples(50, scam_ratio)
            translated_samples = translate_texts(english_samples, translator)

            for (en, ms, label) in translated_samples:
                if not is_valid_translation(en, ms):
                    continue
                index = len(records)
                audio_path = f"data/audio/sample_{index:05d}.wav"
                text_to_wav(ms, audio_path)

                records.append({
                    "id": f"sample_{index:05d}",
                    "english": en,
                    "malay": ms,
                    "label": label,
                    "audio_path": audio_path
                })

                pbar.update(1)

                if len(records) % 10 == 0:
                    df = pd.DataFrame(records)
                    df.to_csv("data/transcripts.csv", index=False)

    df = pd.DataFrame(records)
    df.to_csv("data/transcripts.csv", index=False)
    print(" Dataset generation complete!")

if __name__ == "__main__":
    main()
