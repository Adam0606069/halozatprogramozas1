#Teljes nevet bekérni, monogrammot kell kiíratni

kettobetus=["gy","cs","dz","ly","ny","sz","ty","zs"]
harombetus=["dzs"]

nev=input("Kérek egy teljes nevet: ")

nevek=nev.split()

monogram=""

for szo in nevek:
    if szo[:3] in harombetus:
        monogram+=szo[:3].capitalize()
    elif szo[:2] in kettobetus:
        monogram+=szo[:2].capitalize()
    elif szo:
        monogram+=szo[0].upper()

print(monogram)

# print(f"A monogrammod: {monogram}.")

