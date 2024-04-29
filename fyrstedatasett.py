from Datasett import ResultatKjemiOL
import json

folder = r"C:\Users\78weikri\OneDrive - Akademiet Norge AS\Programmering\kjemAI\Datasett\KjemiOL LK20 R1\\"
datasett = "datasett.txt"

json_data = json.load(open("gpt_test.json", "r"))
resultat2 = ResultatKjemiOL(**json_data)

riktige_svar = 0
antal_oppgaver = 0

for key in resultat2.oppgaver:
    oppgave = resultat2.oppgaver[key]
    antal_oppgaver += 1
    if oppgave.fasit == oppgave.testresultat["gpt-4-turbo"]:
        riktige_svar += 1
print(f"Riktige svar: {riktige_svar}/{antal_oppgaver} ({riktige_svar/antal_oppgaver*100:.2f}%)")


# resultat2.test_gpt4_turbo()

# with open("gpt_test.json", "w") as f:
#     f.write(resultat2.model_dump_json())

# print(resultat2)

