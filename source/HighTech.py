
from Planet import Planet
import random

class HighTech(Planet):
   
    def __init__(self):
        super().__init__()
        self.setPrices()
    
    def setPrices(self):
        self.prices['Bier'] =  random.randint(10,15)
        self.prices['Gold'] = random.randint(100,150)
        self.prices['Weizen'] = random.randint(25,35)
        self.prices['Wasser'] = random.randint(3,7)
