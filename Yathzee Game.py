import random


def xstr(s):
    return '' if s is None else str(s)


def yathzee_game():
    strategie_scelte = []
    punti = 0
    punti_superiori = 0
    turno = 0
    yhatzee_bonus = 0
    punti_strat_1 = None
    punti_strat_2 = None
    punti_strat_3 = None
    punti_strat_4 = None
    punti_strat_5 = None
    punti_strat_6 = None
    punti_strat_7 = None
    punti_strat_8 = None
    punti_strat_9 = None
    punti_strat_10 = None
    punti_strat_11 = None
    punti_strat_12 = None
    punti_strat_13 = None
    while turno < 13:
        turno = turno + 1
        print(f"\nTURNO NUMERO {turno}\n")
        dadi = []
        dadi_rimasti = []
        for i in range(5):
            dadi.append(random.randint(1, 6))
        dadi.sort()
        print(dadi)
        scelta = "a"
        lancio = 1
        while scelta != "s":
            scelta = input("\nPremi 't' per tenere dei dadi, \nPremi 'l' per lanciare di nuovo"
                           "\nPremi 's' per smettere di tirare e scegliere una combinazione"
                           "\nPremi 'i' per avere info sui tuoi punti\n\n")

            if scelta == "i":
                print(f"\nDadi con 1 ---> {xstr(punti_strat_1)}"
                      f"\nDadi con 2 ---> {xstr(punti_strat_2)}"
                      f"\nDadi con 3 ---> {xstr(punti_strat_3)}"
                      f"\nDadi con 4 ---> {xstr(punti_strat_4)}"
                      f"\nDadi con 5 ---> {xstr(punti_strat_5)}"
                      f"\nDadi con 6 ---> {xstr(punti_strat_6)}"
                      f"\n"
                      f"\nTotale punti superiori (>63 per bonus) ---> {punti_superiori}"
                      f"\nPunti mancanti per il bonus            ---> {63 - punti_superiori}"
                      f"\n"
                      f"\n3 dadi uguali    ---> {xstr(punti_strat_7)}"
                      f"\n4 dadi uguali    ---> {xstr(punti_strat_8)}"
                      f"\nFull             ---> {xstr(punti_strat_9)}"
                      f"\nScala con 4 dadi ---> {xstr(punti_strat_10)}"
                      f"\nScala con 5 dadi ---> {xstr(punti_strat_11)}"
                      f"\nYahtzee          ---> {xstr(punti_strat_12)}"
                      f"\nChance           ---> {xstr(punti_strat_13)}"
                      f"\nYhatzee bonus                          ---> {yhatzee_bonus}"
                      f"\nTotale punti inferiori                 ---> {punti - punti_superiori}"
                      f"\nTotale punti (senza bonus)             ---> {punti}\n\n")

            if lancio >= 3:
                scelta = "s"

            if scelta == 't':
                try:
                    dadi_da_tenere = list(map(int, input("Che dadi vuoi tenere? ").split()))
                except:
                    pass
                dadi_rimasti = []
                dadi_iniziali = dadi.copy()
                try:
                    for i in range(len(dadi_da_tenere)):
                        dadi_iniziali.remove(dadi_da_tenere[i])
                        dadi_rimasti.append(dadi_da_tenere[i])
                except:
                    print("Puoi tenere solo dei dadi che sono usciti ")

            if scelta == "l":
                lancio = lancio + 1
                dadi = dadi_rimasti.copy()
                for i in range(5 - len(dadi)):
                    dadi.append(random.randint(1, 6))
                dadi.sort()
                print(dadi)

            if scelta == "s":
                while True:
                    try:
                        print("Scegli la tua strategia\n")
                        if punti_strat_1 is None:
                            print("Premi 1 ---> Dadi con 1")
                        if punti_strat_2 is None:
                            print("Premi 2 ---> Dadi con 2")
                        if punti_strat_3 is None:
                            print("Premi 3 ---> Dadi con 3")
                        if punti_strat_4 is None:
                            print("Premi 4 ---> Dadi con 4")
                        if punti_strat_5 is None:
                            print("Premi 5 ---> Dadi con 5")
                        if punti_strat_6 is None:
                            print("Premi 6 ---> Dadi con 6")
                        if punti_strat_7 is None:
                            print("Premi 7 ---> 3 dadi uguali")
                        if punti_strat_8 is None:
                            print("Premi 8 ---> 4 dadi uguali")
                        if punti_strat_9 is None:
                            print("Premi 9 ---> Full")
                        if punti_strat_10 is None:
                            print("Premi 10 ---> Scala con 4 dadi")
                        if punti_strat_11 is None:
                            print("Premi 11 ---> Scala con 5 dadi")
                        print("Premi 12 ---> Yahtzee")
                        if punti_strat_13 is None:
                            print("Premi 13 ---> Chance")
                        strategia = int(input("\n\n"))
                    except:
                        continue
                    if strategia in strategie_scelte:
                        if strategia == 12 and punti_strat_12 > 1:
                            pass
                        elif strategia == 12 and punti_strat_12 == 0 and \
                                (dadi == [1, 1, 1, 1, 1]
                                 or dadi == [2, 2, 2, 2, 2] or dadi == [3, 3, 3, 3, 3]
                                 or dadi == [4, 4, 4, 4, 4] or dadi == [5, 5, 5, 5, 5]
                                 or dadi == [6, 6, 6, 6, 6]):
                            print("Anche se hai messo 0 nella casella Yhatzee, puoi comunque usare il jolly Yhatzee.")
                            if dadi[0] in strategie_scelte:
                                while True:
                                    try:
                                        numero_strategia = int(
                                            input("Scegli la strategia da usare come jolly\n\n"))
                                    except:
                                        continue
                                    if numero_strategia in strategie_scelte:
                                        print("Hai già scelto questa strategia")
                                        continue
                                    if numero_strategia not in range(1, 14):
                                        print("Devi scegliere un numero tra 1 e 13")
                                        continue
                                    strategie_scelte.append(numero_strategia)

                                    if numero_strategia == 7 or numero_strategia == 8 or numero_strategia == 13:
                                        var1 = sum(dadi)
                                        globals()['punti_strat_%s' % numero_strategia] = var1
                                        punti = punti + var1
                                        print(f"Punteggio = {var1}")
                                        break

                                    elif numero_strategia == 9:
                                        punti_strat_9 = 25
                                        punti = punti + 25
                                        print("Punteggio = 25")
                                        break

                                    elif numero_strategia == 10:
                                        punti_strat_10 = 30
                                        punti = punti + 30
                                        print("Punteggio = 30")
                                        break

                                    elif numero_strategia == 11:
                                        punti_strat_11 = 40
                                        punti = punti + 40
                                        print("Punteggio = 40")
                                        break

                                    else:
                                        globals()['punti_strat_%s' % numero_strategia] = 0
                                        print("Punteggio = 0")
                                        break
                                break
                            else:
                                print(f"La casella 'dadi con {dadi[0]}' è ancora vuota, quindi va "
                                      f"obbligatoriamente scelta per il jolly")
                                var2 = dadi[0] * 5
                                globals()['punti_strat_%s' % dadi[0]] = var2
                                punti = punti + var2
                                punti_superiori = punti_superiori + var2
                                print(f"Punteggio = {var2}")
                                strategie_scelte.append(dadi[0])
                                break

                        else:
                            print("Hai già scelto questa strategia")
                            continue
                    if strategia not in range(1, 14):
                        print("Devi scegliere un numero tra 1 e 13")
                        continue

                    strategie_scelte.append(strategia)

                    if strategia == 1:
                        punti_strat_1 = 1 * dadi.count(1)
                        punti = punti + punti_strat_1
                        punti_superiori = punti_superiori + punti_strat_1
                        print(f"Punteggio = {punti_strat_1}")
                        break

                    if strategia == 2:
                        punti_strat_2 = 2 * dadi.count(2)
                        punti = punti + punti_strat_2
                        punti_superiori = punti_superiori + punti_strat_2
                        print(f"Punteggio = {punti_strat_2}")
                        break

                    if strategia == 3:
                        punti_strat_3 = 3 * dadi.count(3)
                        punti = punti + punti_strat_3
                        punti_superiori = punti_superiori + punti_strat_3
                        print(f"Punteggio = {punti_strat_3}")
                        break

                    if strategia == 4:
                        punti_strat_4 = 4 * dadi.count(4)
                        punti = punti + punti_strat_4
                        punti_superiori = punti_superiori + punti_strat_4
                        print(f"Punteggio = {punti_strat_4}")
                        break

                    if strategia == 5:
                        punti_strat_5 = 5 * dadi.count(5)
                        punti = punti + punti_strat_5
                        punti_superiori = punti_superiori + punti_strat_5
                        print(f"Punteggio = {punti_strat_5}")
                        break

                    if strategia == 6:
                        punti_strat_6 = 6 * dadi.count(6)
                        punti = punti + punti_strat_6
                        punti_superiori = punti_superiori + punti_strat_6
                        print(f"Punteggio = {punti_strat_6}")
                        break

                    if strategia == 7:
                        try:
                            controllo1 = max(x for x in dadi if dadi.count(x) >= 3)
                            punti_strat_7 = sum(dadi)
                            punti = punti + punti_strat_7
                            print(f"Punteggio = {punti_strat_7}")
                            break
                        except:
                            punti_strat_7 = 0
                            print("Punteggio = 0")
                            break

                    if strategia == 8:
                        try:
                            controllo2 = max(x for x in dadi if dadi.count(x) >= 4)
                            punti_strat_8 = sum(dadi)
                            punti = punti + punti_strat_8
                            print(f"Punteggio = {punti_strat_8}")
                            break
                        except:
                            punti_strat_8 = 0
                            print("Punteggio = 0")
                            break

                    if strategia == 9:
                        try:
                            controllo3 = min(x for x in dadi if dadi.count(x) < 2)
                            punti_strat_9 = 0
                            print("Punteggio = 0")
                            break
                        except:
                            punti_strat_9 = 25
                            punti = punti + 25
                            print("Punteggio = 25")
                            break

                    if strategia == 10:
                        if (1 and 2 and 3 and 4) in dadi or (2 and 3 and 4 and 5) in dadi \
                                or (3 and 4 and 5 and 6) in dadi:
                            punti_strat_10 = 30
                            punti = punti + punti_strat_10
                            print("Punteggio = 30")
                            break
                        else:
                            punti_strat_10 = 0
                            print("Punteggio = 0")
                            break

                    if strategia == 11:
                        if dadi == [1, 2, 3, 4, 5] or dadi == [2, 3, 4, 5, 6]:
                            punti_strat_11 = 40
                            punti = punti + punti_strat_11
                            print("Punteggio = 40")
                            break
                        else:
                            punti_strat_11 = 0
                            print("Punteggio = 0")
                            break

                    if strategia == 12:
                        if dadi == [1, 1, 1, 1, 1] or dadi == [2, 2, 2, 2, 2] or dadi == [3, 3, 3, 3, 3] \
                                or dadi == [4, 4, 4, 4, 4] or dadi == [5, 5, 5, 5, 5] or dadi == [6, 6, 6, 6, 6]:
                            if punti_strat_12 != None:
                                if dadi[0] in strategie_scelte:
                                    while True:
                                        try:
                                            numero_strategia = int(
                                                input("Scegli la strategia da usare come jolly\n\n"))
                                        except:
                                            continue
                                        if numero_strategia in strategie_scelte:
                                            print("Hai già scelto questa strategia")
                                            continue
                                        if numero_strategia not in range(1, 14):
                                            print("Devi scegliere un numero tra 1 e 13")
                                            continue
                                        punti = punti + 100
                                        yhatzee_bonus = yhatzee_bonus + 100
                                        print("Punti extra Yhatzee bonus = 100")
                                        strategie_scelte.append(numero_strategia)

                                        if numero_strategia == 7 or numero_strategia == 8 or numero_strategia == 13:
                                            var1 = sum(dadi)
                                            globals()['punti_strat_%s' % numero_strategia] = var1
                                            punti = punti + var1
                                            print(f"Punteggio = {var1}")
                                            break

                                        elif numero_strategia == 9:
                                            punti_strat_9 = 25
                                            punti = punti + 25
                                            print("Punteggio = 25")
                                            break

                                        elif numero_strategia == 10:
                                            punti_strat_10 = 30
                                            punti = punti + 30
                                            print("Punteggio = 30")
                                            break

                                        elif numero_strategia == 11:
                                            punti_strat_11 = 40
                                            punti = punti + 40
                                            print("Punteggio = 40")
                                            break

                                        else:
                                            globals()['punti_strat_%s' % numero_strategia] = 0
                                            print("Punteggio = 0")
                                            break
                                    break
                                else:
                                    print(f"La casella 'dadi con {dadi[0]}' è ancora vuota, quindi va "
                                          f"obbligatoriamente scelta per il jolly")
                                    var2 = dadi[0] * 5
                                    globals()['punti_strat_%s' % dadi[0]] = var2
                                    punti = punti + var2
                                    punti_superiori = punti_superiori + var2
                                    print(f"Punteggio = {var2}")

                                    strategie_scelte.append(dadi[0])
                                    punti = punti + 100
                                    yhatzee_bonus = yhatzee_bonus + 100
                                    print("Punti extra Yhatzee bonus = 100")
                                    break

                            else:
                                punti_strat_12 = 50
                                punti = punti + 50
                                print(f"Punteggio = 50")
                                break
                        else:
                            if punti_strat_12 != None:
                                print("Hai già scelto questa strategia")
                                continue
                            else:
                                punti_strat_12 = 0
                                print("Punteggio = 0")
                                break

                    if strategia == 13:
                        punti_strat_13 = sum(dadi)
                        punti = punti + punti_strat_13
                        print(f"Punteggio = {punti_strat_13}")
                        break

    if punti_superiori >= 63:
        punti_superiori = punti_superiori + 35
        punti = punti + 35
    print(f"Il gioco è finito. Hai totalizzato {punti} punti, includendo i punti bonus.\n")
    print(f"\nDadi con 1 ---> {punti_strat_1}"
          f"\nDadi con 2 ---> {punti_strat_2}"
          f"\nDadi con 3 ---> {punti_strat_3}"
          f"\nDadi con 4 ---> {punti_strat_4}"
          f"\nDadi con 5 ---> {punti_strat_5}"
          f"\nDadi con 6 ---> {punti_strat_6}")
    if punti_superiori >= 63:
        print(f"\nBONUS OTTENUTO                     ---> 35")
    else:
        print(f"\nBONUS NON OTTENUTO                 ---> 0")
    print(f"\nTotale punti superiori             ---> {punti_superiori}"
          f"\n"
          f"\n3 dadi uguali    ---> {punti_strat_7}"
          f"\n4 dadi uguali    ---> {punti_strat_8}"
          f"\nFull             ---> {punti_strat_9}"
          f"\nScala con 4 dadi ---> {punti_strat_10}"
          f"\nScala con 5 dadi ---> {punti_strat_11}"
          f"\nYahtzee          ---> {punti_strat_12}"
          f"\nChance           ---> {punti_strat_13}"
          f"\nYhatzee bonus                          ---> {yhatzee_bonus}"
          f"\nTotale punti inferiori                 ---> {punti - punti_superiori}"
          f"\nTotale punti                           ---> {punti}\n\n")


yathzee_game()
