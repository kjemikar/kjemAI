# Testing av Gemini her: https://shell.cloud.google.com/?fromcloudshell=true&show=ide%2Cterminal

import base64
import requests
from os import listdir
import time
import tomli

# Load the API key from the config file
with open("config.toml") as f:
    config = tomli.load(f)
    api_key = config["api_key"]
# OpenAI API Key


def rett_alternativ(image_path):
    with open("config.toml") as f:
        config = tomli.load(f)
        api_key = config["api_key"]
# OpenAI API Key

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4-turbo",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Hva er det riktige svaret på flervalgsoppgaven? Gi svaret som bokstaven som er rett uten forklaring og uten parentes. Altså er maks lengde på svaret 1 bokstav."
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    print(image_path[-15:], response.json()["choices"][0]["message"]["content"])
    return response.json()["choices"][0]["message"]["content"]

mappe = r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\KjemiOL\Fleirvalsoppgåver\2024\Runde 1\\"

filliste = listdir(mappe)
filliste.sort()

resultat = []
telling = 0
for filnamn in filliste:
    if telling%4 == 0:
        time.sleep(61)
    image_path = mappe+filnamn
    resultat.append([filnamn, rett_alternativ(image_path)])
    telling += 1
