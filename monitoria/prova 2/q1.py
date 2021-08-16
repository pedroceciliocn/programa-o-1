"""
Q1 – Faça uma subrotina Python do tipo função chamada MultiplicaDigitos, que receba um
número Num inteiro positivo de 6 dígitos como parâmetro, e devolva a multiplicação dos
dígitos não nulos deste número como resultado. Caso Num não seja positivo ou tenha mais de
6 dígitos significativos, a função deve retornar como resultado -1 ou -2, respectivamente.

Dica - O resto da divisão de um número por 10 retorna o dígito mais à direita, enquanto que a
divisão inteira dele por 10 retorna a outra parte. Ex: 1234 % 10 -> 4 e 1234 // 10 -> 123.
Este processo pode ser repetido para recuperar cada um dos dígitos de qualquer número.
OBS - Você pode (ou não) incluir um programa principal para ler um valor de N e testar a sua
função: somente a função será avaliada na correção.
"""

def MultiplicaDigitos(Num):
    if Num < 1:
        return -1
    elif Num > 999999:
        return -2
    else:
        mult = 1
        while Num > 0:
            if Num % 10 != 0:
                mult = mult * (Num % 10)
            Num = Num // 10
    
    return mult

erro = True

while erro:
    try:
        Num = int(input("Digite um número: "))

    except ValueError:
        print("Erro de valor (você digitou algo diferente de um número.")
