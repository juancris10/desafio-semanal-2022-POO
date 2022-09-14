#Enunciado: Enunciado: Escribe una función que calcule si un número dado es un número de Armstrong 
# (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar información al respecto

class Amstrong:
    def __init__(self):
        
        self.num = input("introduce el número")
    def ams(self):    
        sum=0
        for i in self.num:
            sum+=int(i)**3
        if sum==int(self.num):
            return ("es un numero amstrong")
        else:
            return ("no es un numero amstrog")
amstrong = Amstrong()
print(amstrong.ams())