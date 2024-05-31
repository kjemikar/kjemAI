import time
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import base64
from os import listdir

# #Kjemi-OL-greier
# mappe = "/home/kristian_weibye/LLM-tests/2024/Runde 1/"
# filliste = listdir(mappe)
# filliste.sort()
import tomli

def rett_alternativ(image_path):
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
    multimodal_model = GenerativeModel(model_name="gemini-1.0-pro-vision-001")

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
    print(image_path[-15:], response.text)
    if response.text in ["A", "B", "C", "D"]:
        return(response.text)
    elif response.text.strip().capitalize() in ["A", "B", "C", "D"]:
        return(response.text.strip().capitalize())
    else:
        raise ValueError("Could not find a valid answer, provided answer was: "+response.text+" for image: "+image_path[-15:])


#filnamn = "2000_R1_1.png"
# resultat = []
# telling = 0
# for filnamn in filliste:
#     if telling%4 == 0:
#         time.sleep(61)
#     image_path = mappe+filnamn
#     resultat.append([filnamn, rett_alternativ(image_path)])
#     telling += 1
# print(resultat)

if __name__ == "__main__":
    mappe = r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\Programmering\kjemAI\Datasett\KjemiOL LK20 R1\\"
    fil = "2023_R1_01.png"
    print(rett_alternativ(mappe+fil))