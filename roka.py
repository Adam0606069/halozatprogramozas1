# A róka libát lop a faluból, a hét minden napján egyet. Ezek súlyát tároltuk el a libak.txt-ben. A farkas várja a falu határában a rókát és a 3 kg-nál nehezebb libát elveszi, 
# a kisebbeket meghagyja a rókánál.

# 0. Fájl beolvasása
# 1. Hány kiló libát evett a róka a héten?
# 2. Átlagosan hány kilósak a rókánál maradt libák?
# 3. Előfordult-e, hogy a róka legalább 3kg-os libát lopott?
# 4. Előfordult-e, hogy a róka kisebb libát lopott, mint az előző napon?
# 5. Hányadik napon sikerült először 3kg-nál nehezebb libát lopni?
# 6. Volt-e 6kg súlyú liba, ha volt akkor melyik napon?
# 7. Hány liba jutott a héten a farkasnak?
# 8. Hány kilós volt a rókánál maradó legnagyobb libának?

#0. feladat

libak=[]

with open("libak.txt") as fin:
    for suly in fin:
        libak.append(int(suly.strip()))

print(libak)

#1. feladat

rokae=0

for suly in libak:
    if suly<=3:
        rokae+=suly

print(f"{rokae} kiló libát evett a róka.")

#2. feladat


rokae_db=0

for liba in libak:
    if liba<=3:
        rokae_db+=1
print(f"A blabla bla {rokae/rokae_db}")

#3. feladat
#Eldöntés tétel

van=False

for liba in libak:
    if liba>=3:
        van=True
        break

if van==True:
    print("Előfordult")
else:
    print("Nem fordult elő")