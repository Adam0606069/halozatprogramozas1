lista=[1,4,5,6,12,80,5,1]

osszeg=0

for szam in lista:
    osszeg+=szam

print(f"A számok összege {osszeg}.")

darab=0

for szam in lista:
    darab+=1

print(f"A számok darab száma {darab}.")

paros=[]

for szam in lista:
    if szam%2==0:
        paros.append(szam)

print(f"A páros számok: {paros}.")

paratlan_db=0

for szam in lista:
    if szam%2!=0:
        paratlan_db+=1

print(f"A páratlan számok: {paratlan_db}.")

#Keresztnevek bekérdezése, amíg nem egyezik

keresztnevek=[]


while True:
    be_nev=input("Kérem a keresztnevet: ")
    if be_nev in keresztnevek:
        break
    keresztnevek.append(be_nev)
print(keresztnevek)