
from abc import ABC
import random
import string

class Planet(ABC):
    
    def __init__(self):
        
        super().__init__()
        prices = {'Bier': 0, 'Gold': 0, 'Weizen': 0, 'Wasser': 0}
        self.prices = prices
        self.name = ''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(5))
          
    def getPrices(self):
        return self.prices
    
    
    def setPrices(self):
        pass
    
    def getName(self):
        return self.name 