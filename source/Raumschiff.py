from abc import ABC

class Raumschiff(ABC):
    def __init__(self):
        self.price = 100
     
    def getPrice(self):
        return self.price