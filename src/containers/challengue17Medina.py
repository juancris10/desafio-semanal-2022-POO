class Runner():
    def __init__(self,estado,pista):
        self.estado=estado
        self.pista=pista
        
    def running(self):
        list_pista = self.pista.split(' ')
        array_runner= self.estado.split(",")
        for i in range(len(list_pista)):
            if array_runner[i]=='run' and list_pista[i]=='_':
                fin = True
            elif array_runner[i]=='jump' and list_pista[i]=='|':
                fin = True
            else:
                if list_pista[i] == '_':
                    list_pista[i]='x'
                    fin=False
                    aux = ''.join(list_pista)
                    print(aux)
                    break
                else:
                    list_pista[i]='/'
                    fin=False
                    aux = ''.join(list_pista)
                    print(aux)
                    break
            aux = ' '.join(list_pista)
            return fin


corredor = Runner("run,run,jump,jump,jump,run,run,jump", '_ _ _ | | _ _ |') 
print(f'terminó la carrera: {corredor.running()} ')
