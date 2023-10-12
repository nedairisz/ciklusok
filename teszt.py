# Eljárásaink tesztelésére

import eljarasok

# Tesztesetek
print("1. teszteset: Pozitív számok")
eljarasok.hanyados(3,5)

print("2. teszteset: Negatív számok")
eljarasok.hanyados(-5,-2)

print("3. teszteset: Tört számok. Nem jó testeset, mert egész számokat vár paraméterként.")
# eljarasok.hanyados(5.2,2.2)

print("4. teszteset: Nincs paraméter")
eljarasok.hanyados() # adtunk alapértelmezett értéket

print("5. teszteset: számláló 0, a=0")
eljarasok.hanyados(0,5)

print("6. teszteset: a nevező 0, b=0 ")
eljarasok.hanyados(-5,0)

