#Enunciado: Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.

class Factorial():
    def __init__(self,numero) :
        self.numero=numero        
    
    def fn_fact(self,numero2):
        self.numero=numero2
        if self.numero == 0:
            return 1
        else:
            return self.numero * self.fn_fact(self.numero-1)
        
fac= Factorial(5)

print(f"el factorial de {fac.numero} es {fac.fn_fact(fac.numero)} " )