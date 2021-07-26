"""
Fazer um programa para achar todos os números
palíndromos entre 100 e 5000.
    – Um número é palíndromo se ele tiver o mesmo valor
        quando escrito da direita para a esquerda. Ex: 17371.
    – Escreva e utilize uma subrotina cujo resultado é o valor
        recebido no parâmetro (int) escrito ao contrário.
• Pode ser interessante utilizar a subrotina da questão
anterior para desmembramento dos números.
"""
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
    fim = len(numero_desmembrado)-1
    i = 0
    while fim > i and numero_desmembrado[i] == numero_desmembrado[fim]:
        fim -= 1
        i += 1
    if numero_desmembrado[i] == numero_desmembrado[fim]:
        return True
    else:
        return False

# print(palindromo(1234554321))
def palindromos_no_intervalo(min, max):
    """função mais genérica para criar
    uma lista com todos os palindromos
    num dado intervalo"""
    lista_palindromos = []
    for numero in range(min, max):
        if palindromo(numero) == True:
            lista_palindromos.append(numero)
    return lista_palindromos

print(palindromos_no_intervalo(100, 5001))

# PL = [palindromo(numero) for numero in range(0,100)]

# PL = map(palindromo(), numero for numero in range(0, 100))


