
from Planet import Planet
import random

class Landwirt(Planet):

    def __init__(self):
        
        super().__init__()
        self.setPrices()
    
    def setPrices(self):
        self.prices['Bier'] =  random.randint(2,3)
        self.prices['Gold'] = random.randint(40,50)
        self.prices['Weizen'] = random.randint(4,7)
        self.prices['Wasser'] = 1
        