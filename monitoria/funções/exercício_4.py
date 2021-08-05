"""4) Faça um programa que contenha uma função chamada getSquare. 
Esta função deve receber um valor e retornar a raiz
quadrada deste valor. 
(Teste com valores distintos e certifique-se de que o funcionamento está correto)"""

def getSquare(numero):
    if numero <= 0:
        return
    else:
        return numero ** 0.5

print(getSquare(2))