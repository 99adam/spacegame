
from Planet import Planet
import random

class Industrie(Planet):
    

    def __init__(self):
        
        super().__init__()
        self.setPrices()
    
    def setPrices(self):
        self.prices['Bier'] = random.randint(3,10)
        self.prices['Gold'] = random.randint(50,80)
        self.prices['Weizen'] = random.randint(10,15)
        self.prices['Wasser'] = random.randint(2,5)