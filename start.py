#Feladat: négyzet/téglalap területének számítása!

# print("Négyzet területszámítás")
# a=int(input("Kérem az oldal hosszát! (cm): "))
# print(f"A négyzet területe {a*a}.")
# print("Téglalap területszámítás")
# aoldal=int(input("Kérem az A oldal-t!: "))
# boldal=int(input("Kérem az B oldal-t!: "))
# print(f"A téglalap területe {2*aoldal*boldal}.")

#kerület

def beker(alakzat, oldal):
    oldalhossz=int(input(f"Kérem a {alakzat} {oldal} oldalának hosszát [cm]: "))

def teglalapterulete(a,b):
    '''kiszámolja az "A" és "B" oldal ismeretlen téglalap területét.'''

#input
mit=input("[T]églalap vagy [N]égyzet kerületét számoljam? {T|N}?")

if mit.upper() == "N":
    alap=int(input("Kérem a négyzet alapját [cm]: "))
    kerulet=4*alap
    print(f"A négyzet kerülete: {kerulet}cm")
elif mit.upper() =="T"    
    a_oldal=beker("téglalap","a")
    b_oldal=beker("téglalap","b")
    kerulet=2*(a_oldal + b_oldal)
    print(f"A téglalap kerülete: {kerulet}cm")
else:
    print("Hibás választás. Kilépek!")