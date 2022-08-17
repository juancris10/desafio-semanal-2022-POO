


lstP=[]
lstP1=[]

lstL=[]
lstL1=[]

pal1= input("Ingrese una palabra")
pal2= input("Ingrese la segunda palabra")


if pal1 == pal2:
    print("Son las mismas palabras")
else:
    lstP.append(pal1)
    lstP1.append(pal2)

    def fnLcdll(p1,p2):
        for i in p1:
            for o in i:
                p2.append(o)

    fnLcdll(lstP,lstL)
    fnLcdll(lstP1,lstL1)
    lstL.sort()
    lstL1.sort()

    if lstL == lstL1:
        print(True)
    else:
        print(False)

