
for n in range(2, 100):##comienza de 2 ya que 1 sabemos que no es numero primo
    for x in range(2, n):
        if n % x == 0: #para que sea primo no debe tener resto 0
            break
    else:
        print(n)
