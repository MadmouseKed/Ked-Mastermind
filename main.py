"""
Wytze A. Ketel 1797080
08/02/2021 13:29
"""
import random
from random import randint


# def evaluatie(gok,code):


# Genereerd code (int) tussen 0 en inclusief opties.
# Maakt hier een lijst van met lengte aantal.
# Minion van spel():
def combinaties1(data):
    resultaat = []
    for a in data:
        for b in data:
            for c in data:
                for d in data:
                    creatie = a+b+c+d
                    resultaat.append(creatie)

    return resultaat

#Update de mogelijkheden lijst, door alle opties die bij voorbaadt niet voldoen aan de eisen te deleten.
def mogelijkhedenUpdate(mogelijkheden, check, gok):
    i = 0
    #deze kleine regel verbeterde de random Ai van 18 naar gemideld 6 gokken.
    try:
        mogelijkheden.remove(gok)
    except ValueError:
        pass
    finally:
        for item in gok:
            if check[i] == '2':
                for mogelijkheid in mogelijkheden:
                    if mogelijkheid[i] != item:
                        mogelijkheden.remove(mogelijkheid)
            elif check[i] == '1':
                for mogelijkheid in mogelijkheden:
                    if item not in mogelijkheid:
                        mogelijkheden.remove(mogelijkheid)
                    elif mogelijkheid[i] == item:
                        mogelijkheden.remove(mogelijkheid)
            elif check[i] == '0':
                for mogelijkheid in mogelijkheden:
                    try:
                        if item in mogelijkheid:
                            mogelijkheden.remove(mogelijkheid)
                    except ValueError:
                        continue

            i += 1
        return mogelijkheden

#Vindt de grootste value in een dictionary en returned dan alleen de bijbehorende key.
def grootsteInDictionary(dictionary):
    key = ''
    waarde = 0
    for sleutel in dictionary:
        if dictionary[sleutel] > waarde:
            key = sleutel
    return key

#Geeft terug een dictionary met daarin hoe vaak een optie voorkomt op plaats index in mogelijkheden.
def MeesteOptiesDictionary(opties, mogelijkheden, index):
    voorkomen = {}
    for optie in opties:
        voorkomen[optie] = 0

    for optie in opties:
        for mogelijkheid in mogelijkheden:
            if optie == mogelijkheid[index]:
                voorkomen[optie] += 1
    return voorkomen

#Geeft terug een gok om te maken, gebaseerd op de mogelijkheden en de opties.
#Het kiest in elke lijn waar feedback niet een 2 is (oftewel goed geraden) het meest voorkomende getal in die lijn.
#Voor 2 (goed gegocht) plaatst ie gewoon gelijk dat getal in. HEt is immers god dus hebben we geen logica voor nodig.
def keuzenGewicht(mogelijkheden, opties, feedback, gokOud):
    index = 0
    gok = ''

    while index < 4:
        if feedback[index] == '2':
            gok += gokOud[index]
        else:
            voorkomen = MeesteOptiesDictionary(opties, mogelijkheden, index)
            keuze = grootsteInDictionary(voorkomen)
            gok += keuze
        index += 1
    return gok

#De comptuer genereert een puur random code met lengte aantal, gebruik makend van de opties.
def aiCode(opties,aantal):
    print("Biep boep. Ik genereer de code!")
    code = ''
    i = 0
    while i < aantal:
        arbitrair = random.randint(0,len(opties)-1)
        code += opties[arbitrair]
        i += 1

    return code

#Als genereerCode, maar ipv randomizer vult de speler de code in.
def spelerCode(opties,aantal):
    i = 0
    code = ''
    print("Maak een code voor de computer.")
    vlag = True
    while vlag:
        print(f"Kies vier cijfers tussen of gelijk aan 0 en 6")
        code = input()
        for item in code:
            if item not in opties:
                print("Sorry dat was geen geldige invoer")
                break
            else:
                vlag = False
    return code

#Vergelijkt gok met code, en vertelt dan hoever je er naast (of juist) zit.
def controle(gok, code):
    feedback = ''
    i = 0
    while i < len(code):
        if gok[i] ==code[i]:
            feedback += '2'
            # feedback.append(2)
        elif gok[i] in code:
            feedback += '1'
            # feedback.append(1)
        else:
            feedback += '0'
            # feedback.append(0)
        i += 1
    return feedback

#Deze print wordt gebruikt in spelerGM, het geeft aan de speler aan hoever de AI is.
#Deze is methode onafhankelijk.
def computerPrint(gok,pogingen,code,controle):
    print(f'poging {pogingen}. \n'
          f'ik heb gegokt {gok}. \n'
          f'Resultaat controle {controle}. \n'
          f'De code is {code}.')



# def superSlechtAI(opties, code):
    #Deze ai gokt elke keer de eerste optie in zijn lijst van mogelijkheden. In weze is er geen sprake van AI, maar gewoon van bruteforcen.

#Mijn AI's
#Deze ai gokt een random mogelijkheid van zijn lijst van mogelijkheden.
def puurRandomAI(opties, code):
    geraden = True
    pogingen = 0
    # Turn 1 hardgecodeerd, de hoop is dat de computer 4 fouten getallen raadt, het aantal mogelijke combinaties dat dan namelijk
    # gegenereerd moet worden om random uit te kiezen wordt dan namelijk aanzienlijk korter.
    # Meestal vindt ie er 2 0en in, het helpt de ai niet, maar limiteerdt vaak wel hoeveel combinaties we moeten genereren.
    T1 = aiCode(opties, 4)
    C1 = controle(T1, code)
    i = 0
    for item in T1:
        # print(f'{item},{T1},{C1},{i},{code}')
        try:
            if C1[i] == '0':
                opties.remove(item)
        except ValueError:
            continue
        i += 1
    mogelijkheden = combinaties1(opties)
    mogelijkheden = combinaties1(opties)
    mogelijkheden = mogelijkhedenUpdate(mogelijkheden, C1, T1)
    pogingen += 1
    # computerPrint(T1, pogingen, code, C1)
    while geraden:
        rKeuze = random.randint(0, len(mogelijkheden) - 1)
        gok = mogelijkheden[rKeuze]
        check = controle(gok, code)
        # print(f'{mogelijkheden} \n'
        #       f'{gok},{check},{code}')
        if check == '2222':
            return gok, pogingen
        else:
            mogelijkheden = mogelijkhedenUpdate(mogelijkheden, check, gok)
            pogingen += 1

#Deze ai begint altijd met de gok '1234' het heeft de meeste kans om perongeluk al wat informatie te krijgen.
def guidedRandomAI(opties, code):
    geraden = True
    pogingen = 0
    # Turn 1 hardgecodeerd, de hoop is dat de computer 4 fouten getallen raadt, het aantal mogelijke combinaties dat dan namelijk
    # gegenereerd moet worden om random uit te kiezen wordt dan namelijk aanzienlijk korter.
    # Meestal vindt ie er 2 0en in, het helpt de ai niet, maar limiteerdt vaak wel hoeveel combinaties we moeten genereren.
    T1 = '1234'
    C1 = controle(T1, code)
    i = 0
    for item in T1:
        # print(f'{item},{T1},{C1},{i},{code}')
        try:
            if C1[i] == '0':
                opties.remove(item)
        except ValueError:
            continue
        i += 1
    mogelijkheden = combinaties1(opties)
    mogelijkheden = mogelijkhedenUpdate(mogelijkheden, C1, T1)
    pogingen += 1
    # computerPrint(T1, pogingen, code, C1)
    while geraden:
        rKeuze = random.randint(0, len(mogelijkheden) - 1)
        gok = mogelijkheden[rKeuze]
        check = controle(gok, code)
        # print(f'{mogelijkheden} \n'
        #       f'{gok},{check},{code}')
        if check == '2222':
            return gok, pogingen
        else:
            mogelijkheden = mogelijkhedenUpdate(mogelijkheden, check, gok)
            pogingen += 1

'''
Ai maakt niet meer random een gok, maar een gok gebaseerd op een weight.
Weight wordt bepaalt door alle opties die overzijn te vergelijken per digit en op te tellen.
Daarna kiest ie de digit die de meeste weight heeft.
Idee zijnde dat hij dan de meeste opties kan weghalen als het incorrect is. Totdat er nog maar 1 optie overblijft.
'''
def gewogenAI(opties,code):
    geraden = True
    pogingen = 0
    # Turn 1 hardgecodeerd, de hoop is dat de computer 4 fouten getallen raadt, het aantal mogelijke combinaties dat dan namelijk
    # gegenereerd moet worden om random uit te kiezen wordt dan namelijk aanzienlijk korter.
    # Meestal vindt ie er 2 0en in, het helpt de ai niet, maar limiteerdt vaak wel hoeveel combinaties we moeten genereren.
    gok = '1234'
    feedback = controle(gok, code)
    i = 0
    for item in gok:
        try:
            if feedback[i] == '0':
                opties.remove(item)
        except ValueError:
            continue
        i += 1

    mogelijkheden = combinaties1(opties)
    mogelijkheden = mogelijkhedenUpdate(mogelijkheden, feedback, gok)
    while geraden:
        gok = keuzenGewicht(mogelijkheden, opties, feedback, gok)
        check = controle(gok, code)
        if check == '2222':
            return gok, pogingen
        else:
            mogelijkheden = mogelijkhedenUpdate(mogelijkheden, check, gok)
            pogingen += 1

#Als de speler wilt raden.
def computerGM(opties, aantal):
    code = aiCode(opties, aantal)
    # print(code)
    pogingen = 0
    geraden = True
    while geraden:
        print("Maak een gok.")
        gok = input()
        legaal = True
        for item in gok:
            if item not in opties:
                print("Sorry, dat was geen geldige gok, probeer het nog eens.")
                legaal = False

        if legaal:
            pogingen += 1
            if gok == code:
                print(f"Dat is inderdaad de code! \n"
                      f"Het koste je {pogingen} keer.")
                break
            else:
                feedback = controle(gok, code)
                print(f"Nog niet correct. \n"
                      f"feedback: {feedback} poging: {pogingen}")
    speelDoor()

#Als de speler wilt dat de computer raadt.
def spelerGM(opties, aantal):
    code = spelerCode(opties, aantal)
    print(type(code))
    print(f"Kies een oplosmethode. \n"
          f"1: puur random AI. \n"
          f"2: guided random. \n"
          f"3: gewogenAI.")
    methode = input()
    if methode == '1':
        gok, pogingen = puurRandomAI(opties, code)
    elif methode == '2':
        gok, pogingen = guidedRandomAI(opties, code)
    elif methode == '3':
        gok, pogingen = gewogenAI(opties, code)

    print(f"Heb 'm! \n"
          f"Het antwoord was {gok}. \n"
          f"Het koste {pogingen} pogingen.")

def speelDoor():

    vlag = True
    while vlag:
        print("Wil je nog een keer spelen? 1 voor ja, 2 voor nee.")
        keuze = input()
        if keuze == '1':
            vlag = False
            spel()
        elif keuze == '2':
            print("Bedankt voor het spelen!")
            vlag = False
        else:
            print("Sorry, dat was geen keuze!")

#Opstart, spel handelt de keuzes en wat wanneer aangeroen dient te worden.
def spel():
    print("Ik start het spel!")
    opties = ['1','2','3','4','5','6']
    aantal = 4
    invoer = True
    #Spelmodus kiezen.
    while invoer:
        print("Maak een keuze, voor spelmodus. 1 voor computer als spelmeester, 2 voor gebruiker als spelmeester.")
        spelModi = int(input())
        if spelModi == 1 or 2:
            invoer = False
        else:
            print("Sorry, dat was niet 1 of 2.")

    print(f"spelModi = {spelModi}")
    #Spelmodus, computer genereert de code.
    #Zie computerGM voor verdere uitleg.
    if spelModi == 1:
        computerGM(opties, aantal)
    #spelmodus, speler genereert de code.
    #Zie spelerGM voor verdere uitleg.
    elif spelModi == 2:
        spelerGM(opties, aantal)

# Groen pijltje voor starten. Hoera.
if __name__ == '__main__':
    spel()
    # code = [2,3,5,4]
    # code = '3344'
    # opties = ['1','2','3','4','5','6']
    # gok, pogingen = gewogenAI(opties, code)
    # print(f"Heb 'm! \n"
    #       f"Het antwoord was {gok}. \n"
    #       f"Het koste {pogingen} pogingen.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/