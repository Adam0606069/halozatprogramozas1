szamok=[1,1,2,2,4,5,2,1,3]

#1
# egyes_db=0
# kettes_db=0
# harmas_db=0
# negyes_db=0
# otos_db=0

# for szam in szamok:
#     if szam==1:
#         egyes_db+=1
#     elif szam==2:
#         kettes_db+=1
#     elif szam==3:
#         harmas_db+=1
#     elif szam==4:
#         negyes_db+=1
#     elif szam==5:
#         otos_db+=1

# print(f"1-es számból ennyi van: {egyes_db}.")
# print(f"2-es számból ennyi van: {kettes_db}.")
# print(f"3-as számból ennyi van: {harmas_db}.")
# print(f"4-es számból ennyi van: {negyes_db}.")
# print(f"5-ös számból ennyi van: {otos_db}.")

#2

# for i in range (1,6):
#     print(f"{i}-ből van {szamok.count(i)}")

#3

darab=[0,0,0,0,0]

for szam in szamok:
    darab[szam-1]+=1

# print(darab)


#4

for i in range(len(darab)):
    print(f"{i+1}-bol van {darab[i]}")