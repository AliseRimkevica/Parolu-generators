# Atkartosana ir runa par visas kopejas programmas atkartosanu
atkartosana = 1

while atkartosana == 1:
    a = int(input("Vai vēlaties ģenerēt jaunu paroli (1), vai arī pārbaudīt savas paroles drošību (2)?\n"))
    if a == 1:

        # Par zīmju skaitu
        zSkaits = int(input("Cik garu paroli vēlēsieties izveidot (zīmju skaits)?\n"))
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
                print("Tavs izvēlētais vārds ir:", customVards)
                print("Tavs izvēlētais cipars ir:", customCipars)

            elif vaiVardusCiparus == 'N' or vaiVardusCiparus == 'n':
                # Znachit nebus lietotaja izveleti vardi un cipari
                vaiVardusCiparusAtkartot = 0
                print("parolē NETIKS IEKĻAUTI vārdi un cipari")

        # Te aiziet runa par to vai iekļaut random skaitļus parolē
        vaiDatoraGenCipAtkartot = 1

        while vaiDatoraGenCipAtkartot == 1:

            vaiDatoraGenCip = str(input("Vai vēlaties, lai jaunajā parolē tiktu iekļauti datora ģenerēti cipari (J/N)? \n"))
            if vaiDatoraGenCip == 'J' or vaiDatoraGenCip == 'j':
                vaiDatoraGenCipAtkartot = 0
                print("Jūsu parolē TIKS iekļauti programmas brīvi izvēlēti cipari.")
            elif vaiDatoraGenCip == 'N' or vaiDatoraGenCip == 'n':
                vaiDatoraGenCipAtkartot = 0
                print("Jūsu parolē NETIKS iekļauti programmas brīvi izvēlēti cipari.")

#Te sākas par to vai lietotajs grib simbolus/lielos burtus
        vaiDatoraGenSimbAtkartot = 1
        while vaiDatoraGenSimbAtkartot == 1:

            vaiDatoraGenSimb = input("Vai vēlaties, lai jaunajā parolē tiktu iekļauti datora ģenerēti simboli (J/N)? \n")
            if vaiDatoraGenSimb == 'J' or vaiDatoraGenSimb == 'j':
                vaiDatoraGenSimbAtkartot = 0
                print("Jūsu parolē TIKS iekļauti programmas brīvi izvēlēti simboli.")
            elif vaiDatoraGenSimb == 'N' or vaiDatoraGenSimb == 'n':
                vaiDatoraGenSimbAtkartot = 0
                print("Jūsu parolē NETIKS iekļauti programmas brīvi izvēlēti simboli.")


        vaiLielieBAtkartot = 1
        while vaiLielieBAtkartot == 1:

            vaiLielieB = input("Vai vēlaties, lai jaunajā parolē tiktu iekļauti lielie burti (J/N)? \n")
            if vaiLielieB == 'J' or vaiLielieB == 'j':
                vaiLielieBAtkartot = 0
                print("Jūsu parolē TIKS iekļauti lielie burti.")
            elif vaiLielieB == 'N' or vaiLielieB == 'n':
                vaiLielieBAtkartot = 0
                print("Jūsu parolē NETIKS iekļauti lielie burti.")


        atkartosana = int(input("Vai vēlaties atgriezties uz sākumu (1), vai iziet (2)? \n"))
    elif a == 2:
        # Te vēl nekas nav :)
        print("šeit būs paroles drošības pārbaude")
        atkartosana = int(input("Vai vēlaties atgriezties uz sākumu (1), vai iziet (2)? \n"))
    else:
        atkartosana = 1
