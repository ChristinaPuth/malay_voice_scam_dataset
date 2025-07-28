



import os
import random
from pydub import AudioSegment
from tqdm import tqdm

# Set Path
audio_dir = "data/audio"
bgm_dir = "environmentvoice"
output_dir = "output_with_bgm"
os.makedirs(output_dir, exist_ok=True)

# Obtain the list of background sounds (only MP3 files)
bgm_files = [f for f in os.listdir(bgm_dir) if f.endswith(".mp3")]

# Obtain the list of audio files, maintaining the order (such as 001, 002,...)
audio_files = sorted([f for f in os.listdir(audio_dir) if f.endswith((".wav", ".mp3"))])

# Traverse audio files
for audio_file in tqdm(audio_files, desc=" In the mixing process..."):
    # Load the audio file
    speech_path = os.path.join(audio_dir, audio_file)
    speech = AudioSegment.from_file(speech_path)

    # Randomly select a background sound file
    bgm_name = random.choice(bgm_files)
    bgm_path = os.path.join(bgm_dir, bgm_name)
    bgm = AudioSegment.from_file(bgm_path)

    # Randomly crop or loop the background sound to make it the same length as the voice.
    if len(bgm) > len(speech):
        start = random.randint(0, len(bgm) - len(speech))
        bgm = bgm[start:start + len(speech)]
    else:
        loop_count = len(speech) // len(bgm) + 1
        bgm = (bgm * loop_count)[:len(speech)]

    # Adjust the volume according to the name of the background sound file
    if "park" in bgm_name:
        bgm += 20
    elif "street" in bgm_name:
        bgm -= 10

    # sound mixing
    mixed = speech.overlay(bgm)

    # The output path has the same name as the original file.
    output_path = os.path.join(output_dir, audio_file)
    mixed.export(output_path, format="wav")

print("All the remixes have been completed. The output files have been saved in output_with_bgm/")
