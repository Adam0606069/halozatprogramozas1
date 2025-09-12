# ciklusok

lista=[1,2,3,4,5]

def osszegez(lista):
    osszeg = 0
    for elem in lista:
        osszeg += elem
    return osszeg

def parosszamok(lista):
    parosszam_darab=0
    for paros in lista:
        if paros%2==0:
            parosszam_darab+=1
    return parosszam_darab

print(f"A lista elemeinek összege: {osszegez(lista)}.")

print(f"A lista páros elemeinek darabszáma: {parosszamok(lista)}.")

#Irass ki egy sorba, 5 csillagot

print("*"*5)

for i in range(5):
    print("*", end="")
print()


#Rajzolj piramist!

n=9
space_db=n-1
csillag_db=1
for i in range(n):
    print(" " * space_db, end="")
    print("*" * csillag_db)
    space_db -= 1
    csillag_db +=2