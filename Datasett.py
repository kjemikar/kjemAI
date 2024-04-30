import pydantic
import json
from typing import Dict
from Oppgave import OppgaveKjemiOL, OppgaveEksamen
import os
import time
from LLM_test_gpt4 import rett_alternativ as rett_alternativ_gpt4
from LLM_test_gemini10 import rett_alternativ as rett_alternativ_gemini10
from LLM_test_gemini15 import rett_alternativ as rett_alternativ_gemini15

MODEL_NAMES = ["gpt-4-turbo", "gemini-1.0-pro-vision-001", "gemini-1.5-pro-preview-0409"]

class ResultatKjemiOL(pydantic.BaseModel):
    folder: str
    oppgaver: Dict[str, OppgaveKjemiOL] = dict()

    def implemented_models(prints:bool=False):
        models = ["gpt-4-turbo"]
        if prints:
            print(models)
        return models

    @classmethod
    def verify_dataset(cls, folder:str, dataset:str)->int:
        """Verify that the dataset is formatted correctly and that the files exist.
        The dataset should be a text file with one line for each image file followed by the correct answer.
        The correct answer should be one of A, B, C, or D.
        The image files should be png files.

        Args:
            folder (str): The folder where the dataset is located.
            dataset (str): The filename of the dataset.

        Raises:
            ValueError: If the dataset is not formatted correctly or the files do not exist.
        
        Returns:
            int: 0 if the dataset is valid.
        """
        if not os.path.exists(folder+dataset):
            raise ValueError(f"Dataset {dataset} does not exist")
        with open(folder+dataset, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) != 2:
                    raise ValueError(f"Line {line} in dataset {dataset} is not formatted correctly")
                if not os.path.exists(folder+parts[0]):
                    raise ValueError(f"File {parts[0]} in dataset {dataset} does not exist")
                if not parts[1] in ["A", "B", "C", "D"]:
                    raise ValueError(f"Alternativ {parts[1]} in dataset {dataset} is not valid")
                if not parts[0].endswith(".png"):
                    raise ValueError(f"File {parts[0]} in dataset {dataset} is not a png file")
        return 0
    
 
    @classmethod
    def from_dataset(cls, folder:str, dataset:str):
        cls.verify_dataset(folder, dataset)
        result = cls(folder=folder)
        with open(folder+dataset, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) == 2:
                    oppgave = OppgaveKjemiOL.fromFilename(parts[0], parts[1])
                    result.oppgaver[oppgave.getFilename()] = oppgave
        return result
    
    def __len__(self):
        return len(self.oppgaver)
        

    def test_gpt4_turbo(self, strengkrav:str=""):
        modell = "gpt-4-turbo"
        val = 0
        for oppgave in self.oppgaver.values():
            if modell not in oppgave.testresultat and strengkrav in oppgave.getFilename():
                image_path = self.folder+oppgave.getFilename()
                oppgave.leggTilTestresultat(modell, rett_alternativ_gpt4(image_path))
                val += 1
                if val %4 == 0: #Avoiding rate limiting
                    time.sleep(60)
        return 0

    def test_gemini10(self):
        modell = "gemini-1.0-pro-vision-001"
        val = 0
        for oppgave in self.oppgaver.values():
            val += 1
            if val %4 == 0:
                time.sleep(60)
            if modell not in oppgave.testresultat:
                image_path = self.folder+oppgave.getFilename()
                oppgave.leggTilTestresultat(modell, rett_alternativ_gemini10(image_path))
        return 0
    
    def test_gemini15(self):
        modell = "gemini-1.5-pro-preview-0409"
        val = 0
        for oppgave in self.oppgaver.values():
            val += 1
            if val %4 == 0:
                time.sleep(60)
            if modell not in oppgave.testresultat:
                image_path = self.folder+oppgave.getFilename()
                oppgave.leggTilTestresultat(modell, rett_alternativ_gemini15(image_path))
        return 0

    def print_comprehensive_report(self):
        pass

    
