# Malay Voice Scam Dataset Generator

This project generates a labeled **Malay-language voice dataset** for scam vs. legitimate phone call scenarios. It synthesizes English text using OpenAI's GPT API, translates it to Malay, and converts it to speech using TTS models. Optionally, background noise is added to simulate realistic phone audio.

---

##  Features

- English scam/legal sentence generation using OpenAI GPT
- Translation from English to Malay using Hugging Face models
-  Text-to-speech synthesis:
  - `gTTS` for fluent rhythm
  - `Coqui TTS xtts_v1.1` for multi-speaker voice variation (optional)
- Environmental background mixing (e.g., street, park)
- Final CSV includes: ID, English, Malay, Label, Audio Path

---

##  Project Structure
```
malay_voice_scam_dataset/
│
├── data/
│ ├── audio/ # Generated voice samples (.wav)
│ └── transcripts.csv # Final metadata CSV
│
├── environmentvoice/ # Background noise clips (e.g., park.mp3)
├── output_with_bgm/ # Audio with mixed background
│
├── utils/
│ ├── init_.py
│ ├── ai_generator.py # English text generation (OpenAI)
│ ├── translator.py # English → Malay translation
│ └── tts.py # TTS synthesis via gTTS or Coqui
│
├── generate_with_bgm.py # Script to add background noise
├── pipeline.py # Main pipeline to generate dataset
├── requirements.txt # Python package dependencies
└── README.md
```
---

##  Getting Started

### 1. Environment Setup

```bash
python -m venv malay-tts-env
source malay-tts-env/bin/activate
pip install -r requirements.txt
```
### 1. Environment Setup
Create a .env file with your OpenAI key:
OPENAI_API_KEY=your_openai_api_key_here

## Run the Pipeline
### Generate the Dataset
```bash
python pipeline.py
```
This script will:

1. Generate English scam & legal sentences

2. Translate them to Malay

3. Convert Malay text to speech (.wav)

4. Save audio + metadata to data/transcripts.csv


###  Add Background Noise 
Make sure environmentvoice/ contains .mp3 files like street.mp3, park.mp3.
```bash
python background.py
```

Outputs are saved to output_with_bgm/.
