#fiu nevei:
# hany % a fiuk aranya

nevek=["Tibi","Évi","Fernando","Karcsi"]
nemek=[1,2,2,1]

# for i in range(len(nevek)):

fiunevek=[]
for i in range(len(nevek)):
    if nemek[i]== 1:
        fiunevek.append(nevek[i])

print(fiunevek)
print(f"{len(fiunevek)} fiú van")

print(f"{len(fiunevek)/len(nevek)*100}% a fiúk aránya.")