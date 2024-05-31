import base64
import requests
import tomli
import vertexai
from vertexai.generative_models import GenerativeModel, Part, GenerationResponse

def generate_response_openai(prompt:str, model:str, image_path:str = "", max_tokens:int = 300)->requests.Response:
    with open(r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\Programmering\kjemAI\crap.toml", "rb") as f:
        config = tomli.load(f)
        api_key = config["api_key"] # OpenAI API Key

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": model,
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": prompt
            }
        ]
        }
    ],
    "max_tokens": max_tokens
    }
    if image_path:
        # Getting the base64 string
        base64_image = encode_image(image_path)
        payload["messages"][0]["content"].append(
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            })

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response
def generate_response_vertexai(prompt:str, model:str, image_path:str = "", uri:str = "")-> GenerationResponse:
    with open(r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\Programmering\kjemAI\crap.toml", "rb") as f:
        config = tomli.load(f)
        project_id = config["project_id"]
    location = "europe-north1"

    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)

    # Load the model
    multimodal_model = GenerativeModel(model_name=model)
    payload = [prompt]
    if image_path:
        with open(image_path, "rb") as image_file:
            data = base64.b64encode(image_file.read())
        payload.append(Part.from_data(mime_type="image/png",data = base64.b64decode(data)))
    if uri:
        payload.append(Part.from_uri(uri, mime_type="image/png"))

    # Query the model
    response = multimodal_model.generate_content(payload)

    return response