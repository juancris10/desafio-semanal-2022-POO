# Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta. 
# - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro. 
# - Expresión balanceada: { [ a * ( c + d ) ] - 5 } - Expresión no balanceada: { a * ( c + d ) ] - 5 }


def fn_balance(expression): 
      
    exp_abiertas = tuple('({[') 
    exp_cerradas = tuple(')}]') 
    map = dict(zip(exp_abiertas, exp_cerradas)) 
    cola = [] 
  
    for i in expression: 
        if i in exp_abiertas: 
            cola.append(map[i]) 
        elif i in exp_cerradas: 
            if not cola or i != cola.pop(): 
                return "Expresión no balanceada"
    if not cola: 
        return "Expresión balanceada"
    else: 
        return "Expresión no balanceada"
  
string = " { [ a * ( c + d ) ] - 5} }"
print(string, "-", fn_balance(string)) 
  
string = "{ a * ( c + d ) ] - 5 }"
print(string,"-", fn_balance(string))


