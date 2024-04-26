import dataclasses
import json
from Oppgave import OppgaveKjemiOL, OppgaveEksamen
from LLM_test_gpt4 import rett_alternativ

MODEL_NAMES = ["gpt-4-turbo"]

@dataclasses.dataclass
class ResultatKjemiOL:

    def implemented_models(prints:bool=False):
        models = ["gpt-4-turbo"]
        if prints:
            print(models)
        return models

    def __init__(self, folder:str):
        self.folder = folder
        self.oppgaver = dict()

    def __str__(self):
        return f"Resultat: {self.folder} {self.oppgaver}"
    
    @classmethod
    def from_dataset(cls, folder:str, dataset:str):
        result = cls(folder)
        with open(dataset, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    oppgave = OppgaveKjemiOL.fromFilename(parts[0], parts[1])
                    result.oppgaver[oppgave.getFilename()] = oppgave
        return result
    
    def __len__(self):
        return len(self.oppgaver)

    #export to json
    def export_to_json(self):
        if len(self.oppgaver) != 0:
            with open(f"{self.folder}.json", "w") as f:
                json.dump(self.oppgaver, f, indent=4)
        else:
            print("No data to export")

        

    @classmethod
    def from_json(cls, folder,filename:str):
        result = cls(folder)
        with open(filename, "r") as f:
            result.oppgaver = json.load(f)
        return result
        
    
    def test_gpt4_turbo(self):
        modell = "gpt-4-turbo"
        for oppgave in self.oppgaver.values():
            if modell not in oppgave.testresultat:
                image_path = self.folder+oppgave.getFilename()
                oppgave.leggTilTestresultat(modell, rett_alternativ(image_path))
        return 0

    def print_comprehensive_report(self):
        pass

    
