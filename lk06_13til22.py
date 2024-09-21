from Datasett import ResultatKjemiOL
import os
import json

folder = r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\Programmering\kjemAI\Datasett\KjemiOL LK06 R1 13til22\\"
datasett = "datasett.txt"

def datasett_fra_filer():
    fillste = os.listdir(folder)
    with open("filliste_alle.txt", "r") as f:
        with open(folder + "datasett.txt", "w") as g:
            for line in f:
                if line.split()[0] in fillste:
                    g.write(line)
 
json_data = json.load(open(folder+"LK06_13til22.json", "r", encoding="utf-8"))
resultat = ResultatKjemiOL(**json_data)

# resultat.print_comprehensive_report()

# for model in resultat.implemented_models():
#     for i in range(13, 23):
#         s = str(2000+i)
#         resultat.get_llm_alternative_simple(model, s)
#         if "LK06_13til22.json" in os.listdir(folder):
#             os.remove(folder + "LK06_13til22.json")
#         with open(folder + "LK06_13til22.json", "w", encoding="utf-8") as f:
#             f.write(resultat.model_dump_json())

# for model in resultat.implemented_models():
#     for i in range(13, 23):
#         s = str(2000+i)
#         resultat.get_llm_alternative_forklaring(model, s)
#         if "LK06_13til22.json" in os.listdir(folder):
#             os.remove(folder + "LK06_13til22.json")
#         with open(folder + "LK06_13til22.json", "w", encoding="utf-8") as f:
#             f.write(resultat.model_dump_json())

# for model in resultat.implemented_models():
#     resultat.test_model(model)
#     if f"{model}.json" in os.listdir(folder):
#         os.remove(folder + f"{model}.json")
#     with

# resultat.print_comprehensive_report()
# riktige_svar_gpt4 = 0
# antal_oppgaver = 0

# for key in resultat.oppgaver:
#     oppgave = resultat.oppgaver[key]
#     antal_oppgaver += 1
#     if oppgave.fasit == oppgave.testresultat["gpt-4-turbo"]:
#         riktige_svar_gpt4 += 1
    # if oppgave.fasit == oppgave.testresultat["gemini-1.0-pro-vision-001"]:
    #     riktige_svar_gemini10 += 1
    # if oppgave.fasit == oppgave.testresultat["gemini-1.5-pro-preview-0409"]:
    #     riktige_svar_gemini15 += 1
#print(riktige_svar_gpt4, antal_oppgaver, riktige_svar_gpt4/antal_oppgaver)




# json_data = json.load(open("alle_tre_test.json", "r"))
# resultat2 = ResultatKjemiOL(**json_data)

# resultat2.test_gemini10()
# resultat2.test_gemini15()

# with open("alle_tre_test.json", "w") as f:
#     f.write(resultat2.model_dump_json())

# riktige_svar_gpt4 = 0
# riktige_svar_gemini10 = 0
# riktige_svar_gemini15 = 0
# antal_oppgaver = 0

# for key in resultat2.oppgaver:
#     oppgave = resultat2.oppgaver[key]
#     oppgave.testresultat["gemini-1.0-pro-vision-001"] = oppgave.testresultat["gemini-1.0-pro-vision-001"].strip().capitalize()


# # resultat2.test_gpt4_turbo()

# # with open("gpt_test.json", "w") as f:
# #     f.write(resultat2.model_dump_json())

# # print(resultat2)

