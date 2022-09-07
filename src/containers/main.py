# X 0
# Sirve para manejar de mejor manera cosas complicadas del array
import numpy as np
# Inicia la clase tablero
class Tablero:
    # Funcion de instanciacion
    def __init__(self) -> object:
        # El tablero es una llista de dos dimensiones 3 x 3 
        self.tablero = [["-", "-", "-"],
                        ["-", "-", "-"],
                        ["-", "-", "-"]]
        # Se convierte la lista en un numpy array
        self.tablero = np.array(self.tablero)

    # Se verifica si el espacio a ocupar esta ocupado o no
    def no_hay_ficha(self, x, y) -> bool:
        # si en el tablero esta el "-": retornar Verdadero
        if "-" in self.tablero[x][y]:
            return True
        else:
            return False
        # Si en el tablero no esta el "-" retornar Falso

    # Funcion que se encarga de agregar la ficha al arreglo
    def agregar_ficha(self, x, y, ficha)-> None|str:
        if self.no_hay_ficha(x, y):
            self.tablero[x][y]=ficha
        else:
            print("No se puede jugar esta casilla")

    # Se verifica si la partida se ha ganado
    def tres_en_raya(self):
        # Se recorren las filas en el tablero
        for fila in self.tablero:
            # Se les asigna a variables las fichas
            primera_ficha = fila[0]
            segunda_ficha = fila[1]
            tercera_ficha = fila[2]
            # Para mas claridad declaro una variable tablero (no escribir siempre "self.tablero")
            tablero = self.tablero
            # Se asignan a variables las columnas de el tablero
            primera = tablero[0]
            segunda = tablero[1]
            tercera = tablero[2]
            # si la primera ficha es igual a la segunda y la primera la primera ficha es igual la tercera (y "-" no esta en esa fila)
            if primera_ficha == segunda_ficha and primera_ficha == tercera_ficha and "-" not in fila:
                # Retornar Verdadero y la ficha que gano
                return [True, primera_ficha]

            # Utilizo numpy para encontrar el diagonal y el diagonal inverso del array, luego repito el porceso del IF, (saber si el primero es el segundo etc...)
            elif (list(np.diag(tablero))[0] == list(np.diag(tablero))[1] and list(np.diag(tablero))[0] == list(np.diag(tablero))[2] and "-" not in list(np.diag(tablero))) or (list(np.fliplr(tablero).diagonal())[0] == list(np.fliplr(tablero).diagonal())[1] and list(np.fliplr(tablero).diagonal())[0] == list(np.fliplr(tablero).diagonal())[2] and "-" not in list(np.fliplr(tablero).diagonal())):
                # Si el condicional anterior es Verdadero la funcion retorna Verdadero y la ficha que gano
                return [True, list(np.fliplr(tablero).diagonal())[0] if list(np.fliplr(tablero).diagonal())[0] != "-" and list(np.fliplr(tablero).diagonal())[0] == list(np.fliplr(tablero).diagonal())[1] else list(np.diag(tablero))[0]]
            
            # Aqui repito los dos anteriores condicionales pero en este condicional verifico las columnas
            elif primera[0] == segunda[0] and primera[0] == tercera[0] and "-" not in tablero[0][0:]:
                return [True, primera[0]]
            
            
            elif primera[1] == segunda[1] and primera[1] == tercera[1] and "-" not in tablero[0][0:]:
                return [True, primera[1]]
            
            
            elif primera[2] == segunda[2] and primera[2] == tercera[2] and "-" not in tablero[0][0:]:
                return [True, primera[2]]

            # Si nada de lo anterior ocurre entonces se retornara Falso
            else:
                return [False]

    # Mostrara en pantalla el tablero
    def mostrar_tablero(self):
        # Si no se usa el for en consola se vera [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        for fila in self.tablero:
            print(fila)

# Se declara la clase juego (Aqui se ejecuta toda la logica del juego)
class Juego:
    # funcion de inicializar recibe 3 parametros, el tablero en el que se juega, el primer jugador y el segundo.
    def __init__(self, tablero, jugador_uno, jugador_dos) -> None:
        self.tablero = tablero
        self.jugador_uno = jugador_uno
        self.jugador_dos = jugador_dos
        # Variable usada para saber si el juego esta ganado (False si no se ha ganado(defecto))
        self.juego_ganado = False
        # Variable usada para saber el turno
        self.turno = 1
        # Variable para saber quien gano la partida
    
    # El metodo principal
    def juego(self):
        # Se piden las coordenads que el jugador en turno va a jugar y se verifica que sean enteros y que esten dentro de los limites del array
        coord = self.coordenadas_entrada()
        # Si el usuario ingresa valores invalidos se repetira el turno
        if coord == False or coord == None:
            print("Valor ingresado invalido")
            self.turno +=1
        # Si el usuario ingresa valores validos se agregara la ficha al tablero
        else:
            x, y = coord[0], coord[1]
            # Si el turno es 1, la fucha a agregar sera la ficha del primer jugador, su no sera la ficha del jugador 2
            self.tablero.agregar_ficha(x, y, self.jugador_uno.ficha if self.turno == 1 else self.jugador_dos.ficha)
        
        # Se mostrara el tablero
        print("_____________")
        self.tablero.mostrar_tablero()
        print("-------------")
        print("***********")

        #Se comprobara si el juego esta ganado
        self.comprobar_juego_ganado()
        # sistema de turnos, si el turno es 1
        if self.turno == 1:
            # Sumar uno al turno para que sea el turno del jugador 2
            self.turno += 1
        # Si no
        else:
            # Restarle 1 al turno para que sea el turno del jugador 1
            self.turno -= 1
    
    # Comprueba si el juego se gano    
    def comprobar_juego_ganado(self):
        # Si la ficha del jugador 1 es igual a la ficha que regreso el tres en raya y tres en raya retorna Verdadero
        if self.jugador_uno.ficha in self.tablero.tres_en_raya() and self.tablero.tres_en_raya()[0] == True:
            print(f"El jugador 1 gano, el juego ha terminado")
            # El juego estara ganado
            self.juego_ganado = True

        # Lo mismo que lo anterior pero con el jugador 2
        elif self.jugador_dos.ficha in self.tablero.tres_en_raya() and self.tablero.tres_en_raya()[0] == True:
            print(f"El jugador {self.jugador_dos.jugador} gano, el juego ha terminado")
            self.juego_ganado = True
        
        # Verificar si el juego esta en empate
        # Para esto, el programa revisara si en el tablero ya no quedan espacios libres
        elif "-" not in self.tablero.tablero[0:]:
            print("El juego esta en empate")
            self.juego_ganado = True
    
    def coordenadas_entrada(self):
        # Se preguntan las coordenadas al jugador, de donde quiere jugar su ficha
        x = input(f"Columna (Del 1 al 3) (Ficha del jugador: {self.jugador_uno.ficha if self.turno == 1 else self.jugador_dos.ficha}): ")
        y = input(f"Fila (Del 1 al 3) (Ficha del jugador: {self.jugador_uno.ficha if self.turno == 1 else self.jugador_dos.ficha}): ")
        # Si el input es un digito
        if x.isdigit() and y.isdigit():
            # Y el input esta dentro del rango
            if int(x) in [1, 2, 3] and int(y) in [1, 2, 3]:
                # Retornar las coordenadas en una lista
                return [int(x)-1, int(y)-1] 
            else:
                # Si no retornar Falso
                return False
        # Igual aca, retornar Falso si nada de lo anterior pasa
        else:
            return False
    


class Jugador:
    def __init__(self, ficha, jugador) -> None:
        self.ficha = ficha
        self.jugador = jugador


def main():
    tab = Tablero()
    jugador_uno = Jugador( "X" if input("Que ficha quieres jugar (X por defecto si no elije nada).") == "" else input("Que ficha quieres jugar (X por defecto si no elije nada)."), 1)
    jugador_dos = Jugador("0" if jugador_uno.ficha == "X" else "X", 2)
    juego_main = Juego(tab, jugador_uno, jugador_dos)
    print("_____________")
    tab.mostrar_tablero()
    print("-------------")
    while juego_main.juego_ganado == False:
        juego_main.juego()
    a = input("Crear otro juego?: ").upper()
    if a == "SI":
        main()
        tab.tablero = [["-", "-", "-"],
                       ["-", "-", "-"],
                       ["-", "-", "-"]]
    else:
        print( "Adioos :D")
        exit()


# Practica recomendada, para evitar llamadas sin querer en los imports
if __name__ == "__main__":
    print("BIENVENIDO A TATETI ")
    main()
