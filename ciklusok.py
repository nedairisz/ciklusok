
# bizonyos műveletek ismétlésére való a ciklus
# ciklusváltozó - számlálja, hogy hányszor futott már le a ciklus
# ciklusmag - ismétlendő utasítások
# ciklusfeltétel - itt adjuk meg, h meddig fusson a ciklus

def szamlalos_ciklus1():
    cv: int = 1
    while (cv <= 10):
        print(f"{cv} Többé nem kések, mert lemaradok!")
        cv += 1

    print(cv, "A ciklus után")

def eloltesztelos_ciklus():
    # kérjünk be egy 10-nél nagyobb számot a felhasználótól

    szam: int= int(input("Adjon meg egy 10-nél nagyobb szsámot! :"))
    while szam <= 10:
        print("10-nél nagyobb számot!")
        szam: int = int(input("Adjon meg egy 10-nél nagyobb szsámot! :"))
    print("Végre 10-nél nagyobb!", szam)

print("valami", end=", ")
print("vége")


# készíts külön eljárást
# 1. írd kia a számokat 1 és 10 között a képernyőre egymás mellé
def ciklus1_feladat():
    cv: int = 1
    while (cv <= 10):
        print(f"{cv}", end=", ")
        cv += 1
    print("\n")
ciklus1_feladat()

# 2. írd kia a számokat 20 és 30 között a képernyőre
def ciklus2_feladat():
    cv: int = 20
    while (cv <= 30):
        print(f"{cv}", end=", ")
        cv += 1
    print("\n")
ciklus2_feladat()

# 3. Írd ki a 15 és 25 közötti páros számokat
def ciklus3_feladat():
    cv: int = 15
    while (cv <= 25):
        if cv % 2 == 0:
            print(f"{cv}", end=", ")
        cv += 1
    print("\n")
ciklus3_feladat()

"""
 cv: int = 16
    while (cv <= 25):
        if cv % 2 == 0:
            print(f"{cv}", end=", ")
        cv += 2
ciklus3_feladat()
"""

# 4. Írd ki a számokat egyesével 12 és 30 között fordított sorrendben
def ciklus4_feladat():
    cv: int = 30
    while (cv >= 12):
        if cv % 2 == 0:
            print(f"{cv}", end=", ")
        cv -= 1
    print("\n")
ciklus4_feladat()