import pydantic
from typing import Dict

class OppgaveKjemiOL(pydantic.BaseModel):
    aar: int
    runde: str
    nummer: int
    fasit: str
    testresultat_fleirval_enkel: Dict[str, str] = dict()

    def leggTilTestresultat(self, modell:str, resultat:str):
        self.testresultat_fleirval_enkel[modell] = resultat

    # init from filename + fasit
    @classmethod
    def fromFilename(cls, filename:str, fasit:str):
        if filename.find("XXX") != -1:
            raise ValueError("XXX in filename, not supposed to be in dataset")
        aar = int(filename[0:4])
        if filename.find("R1") != -1:
            runde = "R1"
        elif filename.find("R2") != -1:
            runde = "R2"
        elif filename.find("Finale") != -1:
            runde = "Finale"
        else:
            raise ValueError("Runde not found in filename")
        
        nummer = int(filename[-6:-4])
        fasit = fasit
        return cls(aar=aar, runde=runde, nummer=nummer, fasit=fasit)
    
    def getFilename(self):
        if self.nummer < 10:
            return f"{self.aar}_{self.runde}_0{self.nummer}.png"
        else:
            return f"{self.aar}_{self.runde}_{self.nummer}.png"

if __name__ == "__main__":
    oppgave = OppgaveKjemiOL(2024, "R1", 1, "A")
    print(oppgave)
    print(oppgave.getFilename())

class OppgaveEksamen:
    def __init__(self, aar:int, eksamenskode:str, nummer:int, fasit:str):
        self.aar = aar
        self.eksamenskode = eksamenskode
        self.nummer = nummer
        self.fasit = fasit
        self.testresultat = dict()
