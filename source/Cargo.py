
from Raumschiff import Raumschiff

class Cargo(Raumschiff):
    def __init__(self):
        super().__init__()
        self.cargoSpace = self.price * 5
        
    def getCargoSpace(self):
        return self.cargoSpace