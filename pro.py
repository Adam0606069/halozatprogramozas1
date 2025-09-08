print("Szia", end=" ")
print("Tibi")
print("Szia", "Tóth", "Karcsi", "!", sep="")
print("Szia Tóth Karcsi!")
nev="Tóth Karcsi"
print(f"Szia {nev}!")
print("Szia", "Peti", sep="\n", end="!") #\t
#adattípusok
# int()
# float()
# str()
# bool()
# list()
# set()
print()
print(int("5"))
print(float(5))
print(str(5.0))
print(type(str(5.0)))
print(bool(0))
napok=["hétfő","kedd","szerda"]
print(f"napok: (napok)")
nevek=["Tibi", "Sanyi", "Tibi"]
print(f"nevek: {set(nevek)}")
print(tuple([1,2,3]))

# HF: Git parancsok
# git init: adott mappa verzió követésének indítása 
# git add: Fájl hozzá adása a következő commitoláshoz
# git clone: repository letöltése a helyi eszközre
# git config --global user.name: felhasználónév beállítása
# git config --global user.email: emailcím csatolása, beállítása
# git log: commit előzmények megtekintése
# git commit -m: commit-álni a legfrissebb munkát egy új snapshot-ként
