from posixpath import split

class Palabra():
  def __init__(self, frase_uno):
    self.frase_uno = frase_uno

  def string(self):
    list_frase = self.frase_uno.split(' ')
    
    for i in range(len(list_frase)):
      list_frase[i]=list_frase[i].capitalize()
    
    aux = ' '.join(list_frase)
    return aux

guts= Palabra("Tremendo pro el pibe")

print(guts.string())
