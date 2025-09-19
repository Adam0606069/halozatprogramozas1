#doga

# A.1. Számok összege: 18
# A.2. Páros számok átlaga: 4.67
# AB.3. Sávdiagram:

lista=[2,4,1,8,3]

osszeg=0
paros_osszeg=0
paros_db=0
csillag=0

#összegzés

def osszegzes(osszeg):
    for elem in lista:
        osszeg+=elem
    return osszeg

print(f"A listában lévő számok összege {osszegzes(osszeg)}.")

#átlag

for elem in lista:
    if elem%2==0:
        paros_osszeg+=elem
        paros_db+=1


atlag=(paros_osszeg/paros_db)
print(f"A páros számok átlaga {atlag}.")


#diagram


for i in lista:
    print(i*"*")

