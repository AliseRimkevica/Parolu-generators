# Atkartosana ir runa par visas kopejas programmas atkartosanu
from typing import Any

import string
import re
import random
import secrets

from string import punctuation

atkartosana = 1

print("\n############################################\n")
print("Paroļu ģenerators / paroļu drošības pārbaude\n")
print("Alise Rimkēviča           Niks Rūdolfs Neija\n")
print("############################################\n")

while atkartosana == 1:
    a = int(input("Vai vēlaties ģenerēt jaunu paroli (1), vai arī pārbaudīt savas paroles drošību (2)?\n"))
    if a == 1:

        parole = []
        customVards = ''
        customCipars = ''
        randomCiparsGarums = 0
        randomSimbGarums = 0
        randomLieliBGarums = 0

        # Par zīmju skaitu
        zSkaits = int(input("Cik garu paroli vēlēsieties izveidot (zīmju skaits)(min 3 simb.)?\n"))
        print("parolē būs", zSkaits, "zīmes")

        # Par vārdu / ciparu iekļaušanu jā / nē
        vaiVardusCiparusAtkartot = 1
        # vaiVardusCiparusAtkartot nozīmē vai tikai to jautājumu atkārtot, ja lietotājs ne to ievada
        while vaiVardusCiparusAtkartot == 1:

            vaiVardusCiparus = str(input("Vai vēlaties parolē iekļaut sevis izvēlētu vārdu / ciparus (J/N)?\n"))

            if vaiVardusCiparus == 'J' or vaiVardusCiparus == 'j':
                # Znachit bus lietotaja izveleti vardi un cipari
                vaiVardusCiparusAtkartot = 0
                customVards = str(input("Ievadi sevis izvēlēto vārdu (ievadi Enter, ja nevēlies): \n"))

                customCipars = str(input("Ievadi sevis izvēlēto ciparu (ievadi Enter, ja nevēlies): \n"))

                if len(customVards) + len(customCipars) <= zSkaits:
                    parole.append(customCipars)
                    parole.append(customVards)
                    print("Jūsu izvēlētais vārds ir:", customVards)
                    print("Jūsu izvēlētais cipars ir:", customCipars)
                else:
                    print("Jūsu izvēlētais vārda / cipara salikums ir pārāk garš. \n")
                    vaiVardusCiparusAtkartot = 1

            elif vaiVardusCiparus == 'N' or vaiVardusCiparus == 'n':
                # Znachit nebus lietotaja izveleti vardi un cipari
                vaiVardusCiparusAtkartot = 0
                print("parolē NETIKS IEKĻAUTI Jūsu izvēlēti vārdi un cipari")

        # Te aiziet runa par to vai iekļaut random skaitļus parolē
        vaiDatoraGenCipAtkartot = 1

        while vaiDatoraGenCipAtkartot == 1:

            vaiDatoraGenCip = str(
                input("Vai vēlaties, lai jaunajā parolē tiktu iekļauti datora ģenerēti cipari (J/N)? \n"))
            if vaiDatoraGenCip == 'J' or vaiDatoraGenCip == 'j':
                vaiDatoraGenCipAtkartot = 0
                # te genere random ciparu no 1 lidz 9
                randomCiparsGarums = zSkaits - len(customVards) - len(customCipars) - 2
                for x in range(randomCiparsGarums):
                    ciparini = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
                    randomCipars = str(secrets.choice(ciparini))
                    parole.append(randomCipars)

                print("Jūsu parolē TIKS iekļauti programmas brīvi izvēlēti cipari.")

            elif vaiDatoraGenCip == 'N' or vaiDatoraGenCip == 'n':
                vaiDatoraGenCipAtkartot = 0
                print("Jūsu parolē NETIKS iekļauti programmas brīvi izvēlēti cipari.")

        # Te sākas par to vai lietotajs grib simbolus/lielos burtus
        vaiDatoraGenSimbAtkartot = 1
        while vaiDatoraGenSimbAtkartot == 1:

            vaiDatoraGenSimb = input(
                "Vai vēlaties, lai jaunajā parolē tiktu iekļauti datora ģenerēti simboli (J/N)? \n")
            if vaiDatoraGenSimb == 'J' or vaiDatoraGenSimb == 'j':
                vaiDatoraGenSimbAtkartot = 0
                randomSimbGarums = zSkaits - len(customVards) - len(customCipars) - randomCiparsGarums - 1
                for x in range(randomSimbGarums):

                    simbolini = ['!', '@', '#', '$', '%', '^', '&', '*']
                    simbols = secrets.choice(simbolini)
                    parole.append(simbols)

                print("Jūsu parolē TIKS iekļauti programmas brīvi izvēlēti simboli.")

            elif vaiDatoraGenSimb == 'N' or vaiDatoraGenSimb == 'n':
                vaiDatoraGenSimbAtkartot = 0
                print("Jūsu parolē NETIKS iekļauti programmas brīvi izvēlēti simboli.")

        vaiLielieBAtkartot = 1
        while vaiLielieBAtkartot == 1:

            vaiLielieB = input("Vai vēlaties, lai jaunajā parolē tiktu iekļauti lielie burti (J/N)? \n")
            if vaiLielieB == 'J' or vaiLielieB == 'j':
                vaiLielieBAtkartot = 0
                randomLieliBGarums = zSkaits - len(customVards) - len(
                    customCipars) - randomCiparsGarums - randomSimbGarums
                for x in range(randomLieliBGarums):

                    randomLielaisBurts = secrets.choice(string.ascii_uppercase)
                    parole.append(randomLielaisBurts)

                print("Jūsu parolē TIKS iekļauti lielie burti.")
            elif vaiLielieB == 'N' or vaiLielieB == 'n':
                vaiLielieBAtkartot = 0
                print("Jūsu parolē NETIKS iekļauti lielie burti.")

        for x in range(zSkaits - len(customVards) - len(
                customCipars) - randomCiparsGarums - randomSimbGarums - randomLieliBGarums):

            randomMazaisBurts = secrets.choice(string.ascii_lowercase)
            parole.append(randomMazaisBurts)

        random.shuffle(parole)
        galaParole = ''.join(parole)
        print(galaParole)

        atkartosana = int(input("Vai vēlaties atgriezties uz sākumu (1), vai iziet (2)? \n"))

    elif a == 2:
        # Te sākam testēt esošas paroles drošību
        userPassword = input("Ievadiet paroli, kuru vēlaties pārbaudīt: ")

        if len(userPassword) >= 12:  # testējam paroles garumu
            parolesDrosGarums = 20  # principaa katram drošības līmenim piešķiram noteiktu punktu skaitu
        elif len(userPassword) >= 8:
            parolesDrosGarums = 10
        elif len(userPassword) < 8:
            parolesDrosGarums = 0
        # print(parolesDrosGarums)  # šī rinda tikai testam

        contains_digit = False  # chekojam, vai satur ciparu parole
        parolesDrosCip = 0
        for character in userPassword:
            if character.isdigit():
                contains_digit = True
                parolesDrosCip = 10
            elif character.isdigit():
                contains_digit = False
                parolesDrosCip = parolesDrosCip
        # print(contains_digit, parolesDrosCip)  # šī rinda tikai testam

        contains_upper = False  # pārbaudam vai ir kāds big burts
        parolesDrosBigBurts = 0
        for bigBurts in userPassword:
            if bigBurts.isupper():
                contains_upper = True
                parolesDrosBigBurts = 10
            elif bigBurts.isupper():
                contains_upper = False
                parolesDrosBigBurts = parolesDrosBigBurts
        # print( contains_upper, parolesDrosBigBurts)  # šī rinda tikai testam

        # skatamies vai ir simbols parolee
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if (regex.search(userPassword) == None):
            parolesDrosSimb = 0
        else:
            parolesDrosSimb = 10

        # print(parolesDrosSimb)  # šī rinda tikai testam

        parolesDrosiba = parolesDrosGarums + parolesDrosCip + parolesDrosBigBurts + parolesDrosSimb
        if parolesDrosiba == 50:
            print("Jūsu parole ir ĻOTI DROŠA")
        elif parolesDrosiba >= 40:
            print("Jūsu parole ir DROŠA")
        elif parolesDrosiba >= 30:
            print("Jūsu parole ir VIDĒJA")
        elif parolesDrosiba < 30:
            print("Jūsu parole ir VĀJA")
        atkartosana = int(input("Vai vēlaties atgriezties uz sākumu (1), vai iziet (2)? \n"))
    else:
        atkartosana = 1
