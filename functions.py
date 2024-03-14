import random

def failist_to_dict():
    euroopa_riigid = {}
    with open('riigid_linnad.txt', 'r',encoding='utf-8-sig') as file:
        for i in file:
            riik, pealinn = i.strip().split('-')# в одну строку записал две переменные
            euroopa_riigid[riik] = pealinn
    return euroopa_riigid

euroopa_riigid = failist_to_dict()


def dict_to_failist(_dict):
    with open('riigid_linnad.txt', 'w',encoding='utf-8-sig') as file:
        for k, v in _dict.items():
            file.write(f"{k}-{v}\n") 


def lisa_riigi(riik, pealinn):
    euroopa_riigid[riik] = pealinn 
    return euroopa_riigid

def naita_riiki_pealinna(kusimus):
    if kusimus in euroopa_riigid:
        print(f"Pealinn {kusimus}: {euroopa_riigid[kusimus]}")
    elif kusimus in euroopa_riigid.values():
        riik = next(key for key, value in euroopa_riigid.items() if value == kusimus)#функция next позволяет закончить итерацию. это экономит ресурсы:)). и ещё я использовал сокращенную for in- comprehensions
        print(f"Riik pealinnaga {kusimus}: {riik}")
    else:
        print("Teave pole sõnastikus.")

def lisa_paranda():
    kusimus = input("Sisestage riigi või pealinna nimi: ").capitalize()
    if kusimus in euroopa_riigid:
        uus_pealinn = input(f"Praegune pealinn {kusimus}: {euroopa_riigid[kusimus]}. Sisestage uus pealinn: ").capitalize()
        euroopa_riigid[kusimus] = uus_pealinn
        print(f"Pealinn {kusimus} on uuendatud: {uus_pealinn}")
        return euroopa_riigid
    elif kusimus in euroopa_riigid.values():
        uus_riik = input(f"Praegune pealinn {kusimus}. Sisestage uus riik: ").capitalize()
        riik = next(key for key, value in       euroopa_riigid.items() if value == kusimus)#функция next позволяет закончить итерацию. это экономит ресурсы:)). и ещё я использовал сокращенную for in- comprehensions
        euroopa_riigid[uus_riik] = kusimus
        del euroopa_riigid[riik]
        print(f"Riik koos pealinna {kusimus} nimetati ümber {uus_riik}.")
        return euroopa_riigid
    


def viktroriin():
    oigevastud = 0
    valevastud = 0

    while True:
        kusimus = random.choice(list(euroopa_riigid.keys()))
        vastus = euroopa_riigid[kusimus]

        kasytaja_vastus = input(f"Mis on riigi või pealinna nimi?: {kusimus} - ")

        if kasytaja_vastus.capitalize() == vastus:
            print("Õige! 🎉")
            oigevastud += 1
        else:
            print(f"Vale. Õige vastus on: {vastus}")
            valevastud += 1

        jatk = input("Jätkata? (ja=1/ei=erinivad nupid): ")
        if jatk != "1":
            break
    print(f"Vastasite {oigevastud} küsimusele {oigevastud + valevastud}-st õigesti  ({((oigevastud / (valevastud + oigevastud) * 100)=:.0f}%).")#:.0f округляет результат

def näita_menüüd(menüü):
    numbrid = sorted(menüü.keys())
    for number in numbrid:
        print(f"{number}. {menüü[number]}")
    valik = input("Palun valige number: ")
    if valik in numbrid:
        return valik
    else:
        print("Vigane number. Palun proovige uuesti.")
        return None


menüü = {}
menüü['1'] = "Teama Euroopa riiki või pealinna."
menüü['2'] = "Lisa euroopariiki."
menüü['3'] = "Paranda."
menüü['4'] = "Kontrolli teada."
