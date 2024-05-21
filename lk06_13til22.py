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

json_data = json.load(open(folder+"LK06_test.json", "r"))
resultat = ResultatKjemiOL(**json_data)
resultat.print_comprehensive_report()
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


# for i in range(13, 23):
#     s = str(2000+i)
#     resultat.test_gpt4o(strengkrav=s)
#     if "LK06_test.json" in os.listdir(folder):
#         os.remove(folder + "LK06_test.json")
#     with open(folder + "LK06_test.json", "w") as f:
#         f.write(resultat.model_dump_json())

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

# #validate results
# for key in resultat2.oppgaver:
#     oppgave = resultat2.oppgaver[key]
#     if not (oppgave.testresultat["gpt-4-turbo"] in ["A", "B", "C", "D"]):
#         print(f"Feil svar GPT-4: {oppgave.testresultat['gpt-4-turbo']}")
#     if not (oppgave.testresultat["gemini-1.0-pro-vision-001"] in ["A", "B", "C", "D"]):
#         print(f"Feil svar Gemini-1.0: {oppgave.testresultat['gemini-1.0-pro-vision-001']}")
#     if not (oppgave.testresultat["gemini-1.5-pro-preview-0409"] in ["A", "B", "C", "D"]):
#         print(f"Feil svar Gemini-1.5: {oppgave.testresultat['gemini-1.5-pro-preview-0409']}")

# for key in resultat2.oppgaver:
#     oppgave = resultat2.oppgaver[key]
#     antal_oppgaver += 1
#     if oppgave.fasit == oppgave.testresultat["gpt-4-turbo"]:
#         riktige_svar_gpt4 += 1
#     if oppgave.fasit == oppgave.testresultat["gemini-1.0-pro-vision-001"]:
#         riktige_svar_gemini10 += 1
#     if oppgave.fasit == oppgave.testresultat["gemini-1.5-pro-preview-0409"]:
#         riktige_svar_gemini15 += 1

# print(f"Antal oppgaver: {antal_oppgaver}")
# print(f"Riktige svar GPT-4: {riktige_svar_gpt4}, {riktige_svar_gpt4/antal_oppgaver*100:.2f}%")
# print(f"Riktige svar Gemini-1.0: {riktige_svar_gemini10}, {riktige_svar_gemini10/antal_oppgaver*100:.2f}%")
# print(f"Riktige svar Gemini-1.5: {riktige_svar_gemini15}, {riktige_svar_gemini15/antal_oppgaver*100:.2f}%")





# # resultat2.test_gpt4_turbo()

# # with open("gpt_test.json", "w") as f:
# #     f.write(resultat2.model_dump_json())

# # print(resultat2)

