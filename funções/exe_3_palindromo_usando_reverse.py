def desmembrar(numero):
    """Pega um numero e divide ele em pedaços;
    depois os coloca em ordem numa lista"""
    lista = []
    while numero > 0:
        div = numero // 10
        resto = numero % 10   
        numero = div
        lista.append(resto)
    
    return lista

# print(desmembrar(12345))

# FUNFANDO LEGAL PRA 1 NUMERO ISOLADO
# def palindromo(numero):
#     numero = desmembrar(numero)
#     fim = len(numero)-1
#     i = 0
#     while fim > i and numero[i] == numero[fim]:
#         fim -= 1
#         i += 1
#     if numero[i] == numero[fim]:
#         return True
#     else:
#         return False
# print(palindromo(21712))

def palindromo(numero):
    numero_desmembrado = desmembrar(numero)
    numero_invertido = desmembrar(numero)
    numero_invertido.reverse()
    if numero_desmembrado == numero_invertido:
        return True
    else:
        return False

# print(palindromo(1234554321))
def palindromos_intervalo(min, max):
    """função mais genérica para criar
    uma lista com todos os palindromos
    num dado intervalo"""
    lista_palindromos = []
    for numero in range(min, max):
        if palindromo(numero) == True:
            lista_palindromos.append(numero)
    return lista_palindromos

print(palindromos_intervalo(100, 5001))