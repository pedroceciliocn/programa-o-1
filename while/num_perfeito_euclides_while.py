#Ler um número inteiro e dizer se ele é perfeito ou não.
n = int(input('digite aqui um valor: '))
sequenciaPerfeitos = 2
i = 2
ehPerfeito = False
while n <= 0:
    n = int(input("Dê um número maior que 0: "))
else:
    while n > sequenciaPerfeitos:
        sequenciaPerfeitos = (2 ** (i -1)) * ((2 ** i) - 1)
        i += 1
        if sequenciaPerfeitos == n:
            ehPerfeito = True
        print(sequenciaPerfeitos)

print(ehPerfeito)