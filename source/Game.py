from Fighter import Fighter
from Cargo import Cargo
from Landwirt import Landwirt
from Industrie import Industrie
from HighTech import HighTech
from Planet import Planet
import sys
from random import randint

money = 1000
ships = []
waren = {'Bier' : 0, 'Gold': 0, 'Weizen': 0, 'Wasser': 0}
schiffe = {'Cargo' : 0, 'Fighter' : 0}

name = input("Name: ")
print("Herzlich Willkommen, " + name + "!")
print("")

"Planetauswahl nach der Begrueßung"

def Planetwechsel():
    global aplanet
    
    while(True):
        print("Wähle einen Planeten:")
        wahl = input("Landwirtschaft[a], Industrie[b], technischer Planet[c]")
        if(wahl == "a"):
            aplanet = Landwirt()
            break
        if(wahl == "b"):
            aplanet = Industrie()
            break
        if(wahl == "c"):
            aplanet = HighTech()
            break

        print("Falsche Eingabe!")

def mainMenu():
    while(True):
        print("")
        print("### Willkommen auf dem " + aplanet.__class__.__name__ + "-Planet "+ aplanet.getName() )
        print("")
        print("Konto  " + str(money)+"$")
        print("")
        print("Was möchten Sie tun?")
        
        print("---------------------")
        
        print("[a] Inventar ansehen")
        
        print("---------------------")
        
        print("## EINKAUFEN ##")
        print("[b] Schiff kaufen")
        print("[d] Waren kaufen")
        
        print("---------------------")
        
        print("## VERKAUFEN ##")
        print("[e] Waren verkaufen")
        
        print("---------------------")
        
        print("[f] Zu einem anderen Planeten wechseln")
        
        
        wahl = 0
        wahl = input()
        if(wahl == "b"):
            buyShip()
        if(wahl == "a"):
            checkwaren()    
        if(wahl == "d"):
            Warenkaufen()
        if(wahl == "e"):
            Warenverkaufen()
        if(wahl == "f"):
            reise()

def randomEvent():
    global money
    money = money / 2 
    print("Die Space-Diebe haben angegriffen...FUCK")
    print("")
    print("FUCK - Du hast dein ganzen Geld fast verloren... Pass auf Kamerad")
    print("")
    input("Druck Enter")
   
def reise():
    Planetwechsel()
    if(randint(0,100) > 85):
        randomEvent()
    
def checkwaren():
    for key,value in waren.items():
        print(key +": " + str(value))

def Warenverkaufen(): 
    
    global waren
    global money
    prices = aplanet.getPrices()
    #function
    print("Der Preis lautet")
    for key,value in prices.items():
        print(key +": " + str(value))
    iwahl = input("Was kaufen: Bier[a], Gold[b], Weizen[c], Wasser[d]")
    number = int(input("Wieviel?"))
    if(iwahl == "a"):
        if(waren['Bier'] >= number):
            money = money + (prices['Bier'] * number)
            waren['Bier'] = waren['Bier'] - number
        
    if(iwahl == "b"):
        if(waren['Gold'] >= number):
            money = money + (prices['Gold'] * number)
            waren['Gold'] = waren['Gold'] - number
        
    if(iwahl == "c"):
        if(waren['Weizen'] >= number):
            money = money + (prices['Weizen'] * number)
            waren['Weizen'] = waren['Weizen'] - number
            
    if(iwahl == "d"):
        if(waren['Wasser'] >= number):
            money = money + (prices['Wasser'] * number)
            waren['Wasser'] = waren['Wasser'] - number
        
def Warenkaufen():

    global waren
    global money
    prices = aplanet.getPrices()
    
    print("Der Preis lautet")
    for key,value in prices.items():
        print(key +": " + str(value))
    iwahl = input("Was kaufen: Bier[a], Gold[b] Weizen[c], Wasser[d]")
    number = int(input("Wieviel?"))
    #if(number <= cargoSpaceCalk()):
    if(iwahl == "a"):
        checkmoney = money - (prices['Bier'] * number)
        if(checkmoney >= 0):
            money = money - (prices['Bier'] * number)
            waren['Bier'] += number
        else:
            print("Keine Geld")
                
    if(iwahl == "b"):
        checkmoney = money - (prices['Gold'] * number)
        if(checkmoney >= 0):
            money = money - (prices['Gold'] * number)
            waren['Gold'] += number
        else:
            print("Keine Geld")
                
    if(iwahl == "c"):
        checkmoney = money - (prices['Weizen'] * number)
        if(checkmoney >= 0):
            money = money - (prices['Weizen'] * number)
            waren['Weizen'] += number
        else:
            print("Keine Geld")
                
    if(iwahl == "d"):
        checkmoney = money - (prices['Wasser'] * number)
        if(checkmoney >= 0):
            money = money - (prices['Wasser'] * number)
            waren['Wasser'] += number
        else:
            print("Keine Geld")
            
        input("Druck Enter")
           
def buyShip():
    
    #Variables
    global ships
    global money
    global number
    #function
    print("Was kaufen?")
    print("[a] Fighter Ship")
    print("[b] Cargo Ship")
    print("[c] nichts")
    wahl = input()
    if(wahl == "a" or wahl == "b"):
        if(wahl == "a"):
            ships.insert(len(ships), Fighter()) 
            print("Fighter Schiff gekauft")
            money = money - 700
        if(wahl == "b"):
            ships.insert(len(ships), Cargo())
            money = money - 500
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