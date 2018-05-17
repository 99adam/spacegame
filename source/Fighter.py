
from Raumschiff import Raumschiff

class Fighter(Raumschiff):
    def __init__(self):
        super().__init__()
        self.firepower = self.price * 2

    def getFirepower(self):
        return self.firepower