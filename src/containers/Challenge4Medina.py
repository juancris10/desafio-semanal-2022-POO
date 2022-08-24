

def fnPoligono(opc,p1,p2):
    if opc ==1:
        AreaT= (p1 * p2) / 2
        print("el area del triangulo es ", AreaT)
    elif opc==2:
        AreaC= p1**2
        print("el area de un cuadrado es ", AreaC)
    else:
        AreaR=p1*p2
        print("el area de un rectangulo ", AreaR)

opc= int(input("Ingrese una opción 1= triangulo. \n 2= cuadrado. \n 3= rectangulo"))

if opc ==1:
    base=int(input("ingrese la base"))
    altura=int(input("ingrese la altura"))
    fnPoligono(opc,base,altura)
elif opc ==2:
    lado=int(input("ingrese el lado del cuadrado"))
    lado2 = lado
    fnPoligono(opc,lado, lado2)
else:
    largo=int(input("ingrese el largo"))
    ancho=int(input("ingrese el ancho"))
    fnPoligono(opc,largo,ancho)