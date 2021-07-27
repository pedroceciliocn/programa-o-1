"""
Fazer um programa para:
    – Ler números inteiros positivos de até 5 dígitos (consistir)
        e imprimir quantas vezes o dígito 9 ocorre em cada um.
    – A leitura pára com número negativo ou zero.
    – Escrever subrotina que deve desmembrar o valor do
        número em seus 5 dígitos, retornando o resultado em 
        uma lista de tamanho 5.
– Escrever outra subrotina que usa a anterior e que:
    • Recebe como parâmetros um número positivo até 99999
        e um algarismo inteiro (0 a 9), nesta ordem.
    • Retorne como resultado a quantidade vezes que o
        algarismo aparece no número.
"""
# def desmembrar(numero):
#     """Pega um numero e divide ele em pedaços;
#     depois os coloca em ordem numa lista"""
#     lista = []
#     while numero > 0:
#         div = numero // 10
#         resto = numero % 10   
#         numero = div
#         lista.append(resto)

#     lista.reverse()
#     return lista


def desmembrar(numero):
    """Pega um numero e divide ele em pedaços;
    depois os coloca em ordem numa lista"""
    lista = []
    while numero > 0:
        resto = numero % 10 
        numero = numero // 10
        lista.append(resto)

    lista.reverse()
    return lista
# print(desmembrar(12345)) #teste

def contador_numero(numero, algarismo):
    """Conta quantas vezes um dado número
    aparece num outro número também dado"""
    contador = 0
    numero = desmembrar(numero)
    for i in numero:
        if i == algarismo:
            contador += 1
    return contador
# print(contador_numero(99999, 9)) #teste

N = int(input("Dê o número: "))
while N > 0 and len(str(N)) <= 5:
    print(f"O número 9 aparece {contador_numero(N, 9)} vezes em {N}")
    N = int(input("Dê o número: "))






