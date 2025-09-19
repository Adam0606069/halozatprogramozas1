#kérj be 0 végjelű számokat és irassuk ki az összegüket!

osszeg=0


# while True:
#     beszam=int(input(f"Kérek egy számot: "))
#     if beszam!=0:
#         osszeg+=beszam
#     else:
#         break

# print(osszeg)


while True:
    be = input("Kérek egy számot: ")
    if be == "":
        break
    osszeg += int(be)

print("Összeg:", osszeg)