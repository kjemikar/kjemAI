import base64
import requests
import tomli
import ntpath
import vertexai
from vertexai.generative_models import GenerativeModel, Part

MODELS = ["gpt-4-turbo", "gpt-4o", "gemini-1.5-pro-preview-0409", "gemini-1.0-pro-vision-001", "gemini-1.5-flash-preview-0514"]

def available_models(prints:bool = False):
    if prints:
        print("Available models are:")
        for model in MODELS:
            print(model)
    return list(MODELS)
def model_wait_time(model:str)-> int:
    if "gpt" in model and model in MODELS:
        return 3
    elif "gemini-1.5-pro" in model and model in MODELS:
        return 3
    elif "gemini" in model:
        return 3
    else:
        raise ValueError("Model must be either a valid OpenAI or vertex-AI model. Provided model was: "+model)
def rett_alternativ(model:str, imagepath:str)-> str:
    if "gpt" in model and model in MODELS:
        return _rett_alternativ_gpt(model, imagepath)
    elif "gemini" in model and model in MODELS:
        return _rett_alternativ_gemini(model, imagepath)
    else:
        raise ValueError("Model must be either a valid gpt or gemini model. Provided model was: "+model)
def _rett_alternativ_gemini(model:str, image_path:str)-> str:

    with open(r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\Programmering\kjemAI\crap.toml", "rb") as f:
        config = tomli.load(f)
        project_id = config["project_id"]
    location = "europe-north1"
    prompt = "Hva er det riktige svaret på flervalgsoppgaven? Gi svaret som bokstaven som er rett uten forklaring og uten parentes. Altså er maksimal lengde på svaret 1 bokstav og svaret er blant bokstavene A, B, C og D."
    with open(image_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())
    
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)

    # Load the model
    multimodal_model = GenerativeModel(model_name=model)

    # Query the model
    response = multimodal_model.generate_content(
        [
            # Add an example image
            #Part.from_uri(
            #    "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
            #),
            Part.from_data(mime_type = "image/png",data = base64.b64decode(data)),
            # Add an example query
            #"what is shown in this image?",
            prompt
        ]
    )
    print(model, ntpath.basename(image_path), response.text)
    if response.text in ["A", "B", "C", "D"]:
        return(response.text)
    elif response.text.strip().capitalize() in ["A", "B", "C", "D"]:
        return(response.text.strip().capitalize())
    else:
        raise ValueError("Could not find a valid answer, provided answer was: "+response.text+" for image: "+ntpath.basename(image_path))
def _rett_alternativ_gpt(model:str, image_path:str)-> str:
    with open(r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\Programmering\kjemAI\crap.toml", "rb") as f:
        config = tomli.load(f)
        api_key = config["api_key"] # OpenAI API Key

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')


    # Getting the base64 string
    base64_image = encode_image(image_path)

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
            "text": "Hva er det riktige svaret på flervalgsoppgaven? Gi svaret som bokstaven som er rett uten forklaring og uten parentes. Altså er maksimal lengde på svaret 1 bokstav og svaret er blant bokstavene A, B, C og D."
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
    text = response.json()["choices"][0]["message"]["content"]
    print(model, ntpath.basename(image_path), text)
    if text in ["A", "B", "C", "D"]:
        return text
    elif text.strip().capitalize() in ["A", "B", "C", "D"]:
        return text.strip().capitalize()
    else:
        raise ValueError("Could not find a valid answer, provided answer was: "+text+" for image: "+ntpath.basename(image_path))
def rett_alternativ_med_forklaring(model:str, imagepath:str)-> str:
    if "gpt" in model and model in MODELS:
        return _rett_alternativ_med_forklaring_gemini(model, imagepath)
    elif "gemini" in model and model in MODELS:
        return _rett_alternativ_med_forklaring_gpt(model, imagepath)
    else:
        raise ValueError("Model must be either a valid gpt or gemini model. Provided model was: "+model)
def _rett_alternativ_med_forklaring_gemini()-> str:
    raise NotImplementedError()
def _rett_alternativ_med_forklaring_gpt()-> str:
    raise NotImplementedError()
    
if __name__ == "__main__":
    print("Available test functions are: rett_alternativ(model:str, imagepath:str)")
    print("Usage: rett_alternativ(model:str, imagepath:str)")
    print("Where model is a valid model from the list below and imagepath is the path to the image of a picture of a multiple choice task you want to test")
    available_models(True)