



import os
import random
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def query(prompt, max_tokens=3000):
    """
    Generate text using OpenAI GPT
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9,
            max_tokens=max_tokens,
            top_p=0.95,
            n=1
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f" OpenAI generation failed:\n\n{e}\n")
        return ""


def generate_sms_samples(num_samples=20, scam_ratio=0.5):
    """
    Call the OpenAI API to generate phishing messages and legitimate messages
    return format [(text, label), ...]
    """
    num_scam = int(num_samples * scam_ratio)
    num_legal = num_samples - num_scam

    print(" Generating English samples...")

    scam_prompt = (
        f"Generate {num_scam} realistic scam phone call dialogues. "
        "Each line should represent something a scammer would say on the phone. "
        "Do not include speaker labels like 'Caller:' or 'Victim:'. "
        "Focus on natural spoken language that would appear in real scam calls. "
        "Separate each sentence with a line break."
    )

    legal_prompt = (
        f"Generate {num_legal} realistic legitimate phone call dialogues. "
        "Each line should represent something a real person (e.g., from a bank, doctor, or delivery company) would say on the phone. "
        "Do not include speaker labels. Use natural spoken language. "
        "Separate each sentence with a line break."
    )


    scam_text = query(scam_prompt)
    legal_text = query(legal_prompt)

    def parse(text, label):
        lines = text.split("\n")
        return [(line.strip("-•0123456789. ").strip(), label) for line in lines if line.strip()]

    return parse(scam_text, "scam") + parse(legal_text, "legal")
