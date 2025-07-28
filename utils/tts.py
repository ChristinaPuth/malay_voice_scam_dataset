
# Gtts 
from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_wav(text, filename, lang="ms"):
    tts = gTTS(text=text, lang=lang)
    temp_mp3 = filename.replace(".wav", ".mp3")
    tts.save(temp_mp3)

    audio = AudioSegment.from_mp3(temp_mp3)
    audio.export(filename, format="wav")
    os.remove(temp_mp3)



# #xtts_V1.1

# import random
# from TTS.api import TTS
# from TTS.tts.configs.xtts_config import XttsConfig
# from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
# from TTS.config.shared_configs import BaseDatasetConfig
# from torch.serialization import safe_globals

# with safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs]):
#     tts_model = TTS(
#         model_name="tts_models/multilingual/multi-dataset/xtts_v1.1",
#         progress_bar=False,
#         gpu=False
#     )

# #   Customized list of sound samples (paths relative to the project directory)
# voice_samples = [
#     "voices/voicesample0.wav",
#     "voices/voicesample1.wav",
#     "voices/voicesample2.wav",
#     "voices/voicesample3.wav"
# ]

# #  The selection probability of each sound sample (with a total sum of 1.0)
# voice_weights = [0.25, 0.25, 0.25, 0.25]

# def choose_voice_sample():
#     """Randomly select a sound sample based on the weights."""
#     return random.choices(voice_samples, weights=voice_weights, k=1)[0]

# def text_to_wav(text, filename, language="en"):
#     """
#     Use the Coqui TTS xtts_v2 model to convert the text into speech and save it as a WAV file. 
#     Parameters:
#         text (str): The text to be synthesized
#         filename (str): The path of the output WAV file
#         language (str): The language code of the voice
#     """
#     speaker_wav = choose_voice_sample()

#     tts_model.tts_to_file(
#         text=text,
#         file_path=filename,
#         speaker_wav=speaker_wav,
#         language=language,
#     )
