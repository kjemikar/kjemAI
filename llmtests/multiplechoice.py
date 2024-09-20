import ntpath
import json
from llmtests.generate import generate_response_openai, generate_response_vertexai
from llmtests.prompts import multiple_choice_picture_simple, multiple_choice_picture_reasoning

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
    

def rett_alternativ(model:str, image_path:str)-> str:
    prompt = multiple_choice_picture_simple()

    if "gpt" in model and model in MODELS:
        response = generate_response_openai(prompt=prompt, model=model,image_path=image_path)
        text = response.json()["choices"][0]["message"]["content"]
    elif "gemini" in model and model in MODELS:
        response = generate_response_vertexai(prompt=prompt, model = model, image_path=image_path)
        text = response.text
    else:
        raise ValueError("Model must be either a valid gpt or gemini model. Provided model was: "+model)

    print(model, ntpath.basename(image_path), text)
    text = text.strip()
    if text in ["A", "B", "C", "D"]:
        return text
    elif text.strip(". ").capitalize() in ["A", "B", "C", "D"]:
        return text.strip(". ").capitalize()
    elif any([t.strip().capitalize() in ["A", "B", "C", "D"] for t in text.split()]):
        print("Found answer in text: ", text)
        text = input("Please provide the answer from the text to continue: ")
        if text in ["A", "B", "C", "D"]:
            return text
        else:
            raise ValueError("Could not find a valid answer, provided answer was: "+text+" for image: "+ntpath.basename(image_path)+ " with model: " + model)
    else:
        raise ValueError("Could not find a valid answer, provided answer was: "+text+" for image: "+ntpath.basename(image_path)+ " with model: " + model)

def rett_alternativ_med_forklaring(model:str, image_path:str)-> dict:
    prompt = multiple_choice_picture_reasoning()

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
    #verifying that the json is correctly formatted
    if not "explanation" in text:
        raise ValueError("Json must contain the key 'explanation'. Provided json was: "+str(text))
    if not "answer" in text:
        raise ValueError("Json must contain the key 'answer'. Provided json was: "+str(text))
    if not text["answer"] in ["A", "B", "C", "D"]:
        raise ValueError("Json key 'answer' must be one of the strings 'A', 'B', 'C' or 'D'. Provided json was: "+str(text))
    if len(text) != 2:
        raise ValueError("Json must contain exactly two keys. Provided json was: "+str(text))
    print(model, ntpath.basename(image_path), text['answer'])
    return text


if __name__ == "__main__":
    print("Available test functions are: rett_alternativ(model:str, imagepath:str)")
    print("Usage: rett_alternativ(model:str, imagepath:str)")
    print("Where model is a valid model from the list below and imagepath is the path to the image of a picture of a multiple choice task you want to test")
    available_models(True)
    rett_alternativ_med_forklaring("gpt-4-turbo", r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\Programmering\kjemAI\KjemiOLAlle\2024\Runde 1\2024_R1_04.png")
    rett_alternativ_med_forklaring("gemini-1.5-pro-preview-0409", r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\Programmering\kjemAI\KjemiOLAlle\2024\Runde 1\2024_R1_04.png")