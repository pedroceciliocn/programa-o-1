"""
1 – O Mínimo Múltiplo Comum (MMC) de 2 números inteiros é o menor número inteiro que é
múltiplo de ambos. Escreva uma função em Python que receba 2 números inteiros como
parâmetros e devolva como resultado o MMC destes números (também inteiro).

    Obs1: A função deve supor que os dois números recebidos como parâmetros serão sempre
    informados corretamente, i.e., não é necessário validá-los na função.

    Obs2: Não utilizar nenhuma fórmula matemática para calcular o MMC.
    Esta função deve fazer parte de um programa Python que calcula e imprime o MMC de todos
    os pares de números inteiros positivos M e N informados pelo usuário. A quantidade de pares
    será informada pelo usuário antes de começar a digitar os números. O seu programa só deve
    imprimir os resultados após o usuário digitar todos os pares de números.

    Obs3: Caso o usuário digite algum número incorreto, o seu programa deve pedir para o
    usuário digitá-lo novamente.
"""


def MMC(n1, n2):
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    
    mmc = maior
    while mmc % menor != 0:
        mmc += maior
    
    return(mmc)

# print(MMC(10, 12))

# N = int(input("Dê o número N de pares que você vai inserir: "))
# while N <=0:
#    N = int(input("Dê o número N (positivo) de pares que você vai inserir: "))

# pares = []
# while N > 0:
#     n_1 = int(input("Dê o primeiro número: "))
#     n_2 = int(input("Dê o segundo número: "))
#     pares.append((n_1, n_2))

#     N -= 1

# for par in pares:
#     print(f"MMC entre {par[0]} e {par[1]} é: {MMC(par[0], par[1]):2}")



###  ALTERNATIVA SEM APPEND ################################################
N = int(input("Dê o número N de pares que você vai inserir: "))
while N <=0:
   N = int(input("Dê o número N (positivo) de pares que você vai inserir: "))

pares = [0] * N
while N > 0:
    n_1 = int(input("Dê o primeiro número: "))
    n_2 = int(input("Dê o segundo número: "))
    pares[N - 1] = (n_1, n_2)

    N -= 1

for par in pares:
    print(f"MMC entre {par[0]} e {par[1]} é: {MMC(par[0], par[1]):2}")