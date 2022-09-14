#Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean 
# o no palíndromos. Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a 
# derecha que de derecha a izquierda. NO se tienen en cuenta los espacios, signos de puntuación y tildes. 
# Ejemplo: Ana lleva al oso la avellana.



#palabra= "palabra"
#palabra2 = "aarbalap"

class Palindromo():
    def __init__(self, palabrauno):
        self.palabrauno = palabrauno
        #self.palabrados = palabrauno
        
    def minusc(self):
        var = self.palabrauno.lower()
        var2= var.replace(",", "").replace(".","").replace(" ", "").replace("{","")
        var_reverse= var2[::-1]
        if var2 == var_reverse:
            
            return True
        else:
            return False

ivan = Palindromo("Ana lleva al oso la avellana{{")
print(ivan.minusc())
#reverse = palabra[::-1] 
#if reverse == palabra2:
#    print (True)
#else:
#    print(False)