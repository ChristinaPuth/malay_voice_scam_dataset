

from transformers import pipeline

def get_translator():
    """
    Use the Facebook NLLB model for English → Malay translation.
        Language codes:
        - English: eng_Latn
        - Malay: zsm_Latn
    """
    try:
        translator = pipeline(
            "translation",
            model="facebook/nllb-200-distilled-600M",
            src_lang="eng_Latn",
            tgt_lang="zsm_Latn"
        )
        print(" NLLB translation model has been loaded successfully")
        return translator
    except Exception as e:
        print(f" Failed to load the NLLB translation model: {e}")
        raise e


def translate_texts(samples, translator):
    """
    Translate the English text into Malay in batches, and automatically skip invalid or abnormal text.
    
    parameter
        samples: [(english_text, label), ...]
        translator: Hugging Face pipeline example
    
    RETURN:
        [(english_text, malay_text, label), ...]
    """
    translated = []

    for text, label in samples:
        text = str(text).strip()

        if not text or len(text) < 5 or text.lower() in ["none", "n/a"]:
            print(f" Skip invalid English input: '{text}'")
            result = ""
        else:
            try:
                result = translator(text)[0]["translation_text"]
            except Exception as e:
                print(f"translation failure '{text}'\nreason: {e}")
                result = ""

        translated.append((text, result.strip(), label))

    return translated
