import ntpath
import json
from generate import generate_response_openai, generate_response_vertexai
from prompts import multiple_choice_get_question_keywords
MODELS = ["gpt-4-turbo", "gpt-4o", "gemini-1.5-pro-preview-0409", "gemini-1.0-pro-vision-001", "gemini-1.5-flash-preview-0514"]

def available_models(prints:bool = False):
    if prints:
        print("Available models are:")
        for model in MODELS:
            print(model)
    return list(MODELS)
def model_wait_time(model:str)-> int:
    if "gpt" in model and model in MODELS:
        return 4
    elif "gemini-1.5-pro" in model and model in MODELS:
        return 3
    elif "gemini" in model:
        return 3
    else:
        raise ValueError("Model must be either a valid OpenAI or vertex-AI model. Provided model was: "+model)
    

def get_keywords(model:str, image_path:str)-> dict:
    prompt = multiple_choice_get_question_keywords()

    if "gpt" in model and model in MODELS:
        response = generate_response_openai(prompt=prompt, model=model,image_path=image_path)
        text = response.json()["choices"][0]["message"]["content"]
    elif "gemini" in model and model in MODELS:
        response = generate_response_vertexai(prompt=prompt, model = model, image_path=image_path)
        text = response.text
    else:
        raise ValueError("Model must be either a valid gpt or gemini model. Provided model was: "+model)
    print(text)
    if "```json" in text:
        #splitting the text to get the json part
        text = text.split("```json")[1]
        text = text.replace("```json", "")
        text = text.replace("```", "")
    #replacing the backslashes with empty strings
    text = text.replace("\\", "")
    text = json.loads(text)
    #verifying that the json loads a list of strings
    if not isinstance(text, list)and all([isinstance(t, str) for t in text]):
        raise ValueError("The json did not load a list of strings")
    # Removing duplicates
    text = set(text)
    print(model, ntpath.basename(image_path), text)
    return text



if __name__ == "__main__":
    print("Available test functions are: rett_alternativ(model:str, imagepath:str)")
    print("Usage: rett_alternativ(model:str, imagepath:str)")
    print("Where model is a valid model from the list below and imagepath is the path to the image of a picture of a multiple choice task you want to test")
    available_models(True)
    get_keywords("gpt-4-turbo", r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\Programmering\kjemAI\KjemiOLAlle\2024\Runde 1\2024_R1_04.png")