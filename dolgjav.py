lista=[2,4,1,8,3]

# A1. A lista elemeinek összege

osszeg=0
for szam in lista:
    osszeg+= szam

print(f"A lista elemeinek összege: {osszeg}.")

# B1. A lista elemeinek darabszáma.

darab=0
for szam in lista:
    darab+=1

print(f"A lista elemeinek darabszáma: {darab}")
print(f"A lista elemeinek darabszáma: {len(lista)}")

# A2. Páros számok átlaga.

paros_osszeg=0
paros_db=0

for szam in lista:
    if szam%2==0:
        paros_osszeg+=szam
        paros_db+=1

print(f"A páros számok átlaga {paros_osszeg/paros_db:.3f}.")

#B2. Paros szamok darab szama.

print(f"A páros számok darabszáma: {paros_db}")

#A2 és B2 --> Páros számok kiválogatása.

parosok_lista=[szam for szam in lista if szam %2==0]

# parosok_lista=[2,4,8]
print(f"A paros szamok atlaga {sum(parosok_lista)/len(parosok_lista)}")
print(f"Paros szamok darabszama: {len(parosok_lista)}")

#AB 3. Diagram

for csillag in lista:
    print(csillag*"*")