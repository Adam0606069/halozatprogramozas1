#Kérjük be a számokat és adjuk meg az összegüket.
#1. 0 végjelig
#2. Enter végjelig HF

# osszeg=0
# be=1

# while be!=0:    
#     be=int(input("Kérek egy számot: "))
#     osszeg+=be

# print(osszeg)

# Enter végjel

osszeg = 0

while True:
    be = input("Kérek egy számot: ")
    if be == "":
        break
    osszeg += int(be)

print("Összeg:", osszeg)

#break --> Ciklus megtörése