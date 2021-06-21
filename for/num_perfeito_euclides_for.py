#Ler um número inteiro e dizer se ele é perfeito ou não.
n = int(input('digite aqui um valor: '))
sequenciaPerfeitos = 0
i = 1
ehPerfeito = False
while n <= 0:
    n = int(input("Dê um número maior que 0: "))
else:
    for (i, sequenciaPerfeitos): #isso é uma recursao, daria pra melhorar
        sequenciaPerfeitos = (2 ** (i -1)) * ((2 ** i) - 1)
        if sequenciaPerfeitos == n:
            ehPerfeito = True
        print(sequenciaPerfeitos)

print(ehPerfeito)

