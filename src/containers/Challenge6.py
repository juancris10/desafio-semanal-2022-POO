lst=[]
lst2=[]
def CadenaInvertida(p1,p2):
    for i in range(len(p1)):
        for x in range(len(p1)):
            elemento=p1[-1]
            p2.append(elemento)
            p1.pop()
    print("".join(p2))

palabra="juan"
for i in palabra:
    lst.append(i)

CadenaInvertida(lst,lst2)