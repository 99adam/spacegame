from Fighter import Fighter
from Cargo import Cargo
from Landwirt import Landwirt
from Industrie import Industrie
from HighTech import HighTech
import sys
from random import randint

money = 1000
ships = []
waren = {'Bier' : 0, 'Gold': 0, 'Weizen': 0, 'Wasser': 0}

name = input("Name: ")
print("Herzlich Willkommen, " + name + "!")
print("")

"Planetauswahl nach der Begrueßung"

def Planetwechsel():
    global activePlanet
    
    while(True):
        print("Wähle einen Planeten:")
        choice = input("Landwirtschaft[a], Industrie[b], technischer Planet[c]")
        if(choice == "a"):
            activePlanet = Landwirt()
            break
        if(choice == "b"):
            activePlanet = Industrie()
            break
        if(choice == "c"):
            activePlanet = HighTech()
            break

        print("Falsche Eingabe!")


def mainMenu():
    while(True):
        print("")
        print("### Willkommen auf dem " + activePlanet.__class__.__name__ + "-Planet ###" )
        print("")
        print("Konto  " + str(money)+"$")
        print("")
        print("Was möchten Sie tun?")
        
        print("---------------------")
        
        print("[a] Inventar ansehen")
        
        print("---------------------")
        
        print("## EINKAUFEN ##")
        print("[b] Schiff kaufen")
        print("[c] Cargo Space")
        print("[d] Waren kaufen")
        
        print("---------------------")
        
        print("## VERKAUFEN ##")
        print("[e] Waren verkaufen")
        
        print("---------------------")
        
        print("[f] Zu einem anderen Planeten wechseln")
        
        
        
        choice = 0
        choice = input()
        if(choice == "b"):
            buyShip()
        if(choice == "c"):
            print("CargoSpace  " +str(cargoSpaceCalk()))
            input("[ENTER]")
        if(choice == "a"):
            checkwaren()    
        if(choice == "d"):
            Warenkaufen()
        if(choice == "e"):
            Warenverkaufen()
        if(choice == "f"):
            travel()

def randomEvent():
    money= 0
    "global money"
    print("Du hast " +money+ "$")
    
    print("Dir wurde alles gestohlen!")
        
    input("Druck Enter")
    sys.exit(0)    
    
def travel():
    
    Planetwechsel()
    if(randint(0,5) > 4):
        randomEvent()
    
def checkwaren():
    
    for key,value in waren.items():
        print(key +": " + str(value))

def cargoSpaceCalk():
    
    space = 10
    for s in ships:
        if(s.__class__.__name__ == "Cargo"):
            space += s.getCargoSpace()
    return space

def Warenverkaufen(): 
    
    global waren
    global money
    prices = activePlanet.getPrices()
    #function
    print("Der Preis lautet")
    for key,value in prices.items():
        print(key +": " + str(value))
    ichoice = input("Was kaufen: Bier[a], Gold[b], Weizen[c], Wasser[d]")
    number = int(input("Wieviel?"))
    if(ichoice == "a"):
        if(waren['Bier'] >= number):
            money = money + (prices['Bier'] * number)
            waren['Bier'] = waren['Bier'] - number
        
    if(ichoice == "b"):
        if(waren['Gold'] >= number):
            money = money + (prices['Gold'] * number)
            waren['Gold'] = waren['Gold'] - number
        
    if(ichoice == "c"):
        if(waren['Weizen'] >= number):
            money = money + (prices['Weizen'] * number)
            waren['Weizen'] = waren['Weizen'] - number
            
    if(ichoice == "d"):
        if(waren['Wasser'] >= number):
            money = money + (prices['Wasser'] * number)
            waren['Wasser'] = waren['Wasser'] - number
        
def Warenkaufen():

    global waren
    global money
    prices = activePlanet.getPrices()
    
    print("Der Preis lautet")
    for key,value in prices.items():
        print(key +": " + str(value))
    ichoice = input("Was kaufen: Bier[a], Gold[b] Weizen[c], Wasser[d]")
    number = int(input("Wieviel?"))
    if(number <= cargoSpaceCalk()):
        if(ichoice == "a"):
            checkmoney = money - (prices['Bier'] * number)
            if(checkmoney >= 0):
                money = money - (prices['Bier'] * number)
                waren['Bier'] += number
            else:
                print("Keine Geld")
                
        if(ichoice == "b"):
            checkmoney = money - (prices['Gold'] * number)
            if(checkmoney >= 0):
                money = money - (prices['Gold'] * number)
                waren['Gold'] += number
            else:
                print("Keine Geld")
                
        if(ichoice == "c"):
            checkmoney = money - (prices['Weizen'] * number)
            if(checkmoney >= 0):
                money = money - (prices['Weizen'] * number)
                waren['Weizen'] += number
            else:
                print("Keine Geld")
                
        if(ichoice == "d"):
            checkmoney = money - (prices['Wasser'] * number)
            if(checkmoney >= 0):
                money = money - (prices['Wasser'] * number)
                waren['Wasser'] += number
            else:
                print("Keine Geld")
                
    else:
        print("Kein Platz")
    input("Druck Enter")
           
def buyShip():
    
    #Variables
    global ships
    global money
    #function
    print("Was kaufen?")
    print("[1] Fighter Ship")
    print("[2] Cargo Ship")
    print("[0] niggs")
    choice = input()
    if(choice == "1" or choice == "2"):
        if(choice == "1"):
            ships.insert(len(ships), Fighter()) 
            print("Fighter Schiff gekauft")
        if(choice == "2"):
            ships.insert(len(ships), Cargo())
            print("Cargo Schiff gekauft")

    print("Du hast diese Schiffe ")
    cf = 0
    cc = 0
    for s in ships:
        if(s.__class__.__name__ == "Fighter"):
            cf = cf + 1
        else:
            cc = cc + 1
    print(str(cf) + " x Fighter")
    print(str(cc) + " x Cargo")
    input("Druck Enter")
        
Planetwechsel()
mainMenu()