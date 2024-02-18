from functions import *


euroopa_riigid = failist_to_dict()


vastus = input("Kas sina sovid õppida? ja = 1 /ei = erinivad: ")
if vastus == '1':
    while True:
        option = näita_menüüd(menüü)
        if option == '1':
            vastus_k = input(
                "Millist Euroopa riiki või pealinna tahaksite teada?: ").capitalize()
            naita_riiki_pealinna(vastus_k)
            jatk = input("Продолжать (1) или выйти (2) из словаря? ")
            if jatk == '2':
                print("Head aega!")
                break

        elif option == '2':
            riik = input("Sistage nimi riigi: ").capitalize()
            pealiin = input("Sistage nimi pealiin: ").capitalize()
            uus_dict = lisa_riigi(riik, pealiin)
            dict_to_failist(uus_dict)
            print("Lisatud sõnsastiku.")
            jatk = input("Продолжать (1) или выйти (2) из словаря? ")
            if jatk == '2':
                print("Head aega!")
                break
        elif option == '3':
            uus_dict = lisa_paranda()
            dict_to_failist(uus_dict)
            jatk = input("Продолжать (1) или выйти (2) из словаря? ")
            if jatk == '2':
                print("Head aega!")
                break
        elif option == '4':
            viktroriin()
            jatk = input("Продолжать (1) или выйти (2) из словаря? ")
            if jatk == '2':
                print("Head aega!")
                break

else:
    print("Head aega!")
    exit
