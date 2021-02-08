"""
Wytze A. Ketel 1797080
08/02/2021 13:29
"""
import random
from random import randint


# def evaluatie(gok,code):


#Genereerd code (int) tussen 0 en inclusief opties.
#Maakt hier een lijst van met lengte aantal.
#Minion van spel():
def genereerCode(opties,aantal):
    print("Biep boep. Ik genereer de code!")
    code = []
    i = 0
    while i < aantal:
        arbitrair = random.randint(0,opties)
        code.append(arbitrair)
        i += 1

    return code

#Als genereerCode, maar ipv randomizer vult de speler de code in.
def spelerCode(opties,aantal):
    i = 0
    code = []
    print("Maak een code voor de computer.")
    while i < aantal:
        print(f"Kies een cijfer tussen of gelijk aan 0 en {opties}")
        invoer = input()
        if invoer <= opties & invoer >= 0:
            code.append(invoer)
            i += 1
        else:
            print("Sorry dat was geen geldige invoer")

    return code

#Opstart, spel handelt de keuzes en wat wanneer aangeroen dient te worden.
def spel():
    print("Ik start het spel!")
    opties = 6
    aantal = 4
    invoer = True
    #Spelmodus kiezen.
    while invoer:
        print("Maak een keuze, voor spelmodus. 1 voor computer als spelmeester, 2 voor gebruiker als spelmeester.")
        spelModi = input()
        if spelModi == 1 or 2:
            invoer = False
        else:
            print("Sorry, dat was niet 1 of 2.")

    print(f"spelModi = {spelModi}")
    #Spelmodus, computer genereert de code.
    if spelModi == 1:
        code = genereerCode(opties,aantal)
        print(code)
    #spelmodus, speler genereert de code.
    elif spelModi == 2:
        code = spelerCode(opties, aantal)
        print(code)

# Groen pijltje voor starten. Hoera.
if __name__ == '__main__':
    spel()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/