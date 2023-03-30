import os
import openai
from dotenv import load_dotenv

load_dotenv()

def generateImg(text, sz):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    img = openai.Image.create(
        prompt = text,
        n = 1,
        size = sz
    )

    return img["data"][0]["url"]
