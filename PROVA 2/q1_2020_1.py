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

def MultiplicaDigitos(numero):
    multi_resto = 1
    while numero > 0:
        if len(str(numero)) > 6:
            return -2
        else:
            resto = numero % 10
            numero = numero // 10
            multi_resto *= resto
    while numero < 0:
        return -1
    return multi_resto


# DEPOIS FAZER A FUNÇÃO PRINCIPAL COM TRATAMENTO DE EXCEÇÕES
print(MultiplicaDigitos(25))
print(MultiplicaDigitos(222))
print(MultiplicaDigitos(222222))
print(MultiplicaDigitos(2222222))
print(MultiplicaDigitos(-2))