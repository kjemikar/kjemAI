import pydantic
import json
from typing import Dict
from Oppgave import OppgaveKjemiOL, OppgaveEksamen
import os
import time
from llmtests.multiplechoice import rett_alternativ, available_models, model_wait_time, rett_alternativ_med_forklaring


class ResultatKjemiOL(pydantic.BaseModel):
    folder: str
    oppgaver: Dict[str, OppgaveKjemiOL] = dict()

    def implemented_models(prints:bool=False)->list:
        return list(available_models(prints=prints))
    def tested_models_fleirval_forklaring(self)->list:
        models = list(self.implemented_models())
        for oppgave in self.oppgaver.values():
            for model in models:
                if model not in oppgave.testresultat_fleirval_forklaring:
                    models.remove(model)
        return models
    def tested_models_fleirval_enkel(self)->list:
        models = list(self.implemented_models())
        for oppgave in self.oppgaver.values():
            for model in models:
                if model not in oppgave.testresultat_fleirval_enkel:
                    models.remove(model)
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
        
    def get_llm_alternative_simple(self, model:str, strengkrav:str="")->int:
        """Get the alternative that the model predicts for the image that contains the string in strengkrav.

        Args:
            model (str): The model to use.
            strengkrav (str, optional): The string that the filename must contain. Defaults to "".

        Returns:
            str: The alternative that the model predicts.
        """
        # Verify that the model is implemented
        if model not in self.implemented_models():
            raise ValueError(f"Model {model} is not implemented")
        
        for oppgave in self.oppgaver.values():
            if model not in oppgave.testresultat_fleirval_enkel and strengkrav in oppgave.getFilename():
                image_path = self.folder+oppgave.getFilename()
                oppgave.leggTilTestresultat(model, rett_alternativ(model, image_path))
                time.sleep(model_wait_time(model))
        return 0

    def get_llm_alternative_forklaring(self, model:str, strengkrav:str="")->int:
        """Get the alternatives that the model predicts for the images that contains the string in strengkrav and the explanation and add both to the dict of the tasks called testresultat_fleirval_forklaring.

        Args:
            model (str): The model to use.
            strengkrav (str, optional): The string that the filename must contain. Defaults to "".

        Returns:
            int: 0 if the function runs successfully.

        """
        # Verify that the model is implemented
        if model not in self.implemented_models():
            raise ValueError(f"Model {model} is not implemented")
        
        for oppgave in self.oppgaver.values():
            if model not in oppgave.testresultat_fleirval_forklaring and strengkrav in oppgave.getFilename():
                image_path = self.folder+oppgave.getFilename()
                oppgave.leggTilTestresultatForklaring(model, rett_alternativ_med_forklaring(model, image_path))
                time.sleep(model_wait_time(model))
        return 0
    def print_comprehensive_report(self):
        # print models tested with score per model
        models = self.tested_models_fleirval_enkel()
        print("Models tested without explanation:")
        print(models)
        for model in models:
            print(f"Model: {model}")
            riktige_svar = 0
            antal_oppgaver = 0
            for oppgave in self.oppgaver.values():
                antal_oppgaver += 1
                if oppgave.fasit == oppgave.testresultat_fleirval_enkel[model]:
                    riktige_svar += 1
            print(f"Antall riktige svar: {riktige_svar}")
            print(f"Antall oppgaver: {antal_oppgaver}")
            print(f"Score: {riktige_svar/antal_oppgaver}")
        # print models tested with explanation
        models = self.tested_models_fleirval_forklaring()
        print("Models tested with explanation:")
        print(models)
        for model in models:
            print(f"Model: {model}")
            riktige_svar = 0
            antal_oppgaver = 0
            for oppgave in self.oppgaver.values():
                antal_oppgaver += 1
                if oppgave.fasit == oppgave.testresultat_fleirval_forklaring[model]["answer"]:
                    riktige_svar += 1
            print(f"Antall riktige svar: {riktige_svar}")
            print(f"Antall oppgaver: {antal_oppgaver}")
            print(f"Score: {riktige_svar/antal_oppgaver}")
        # print number of correct answers per model            

