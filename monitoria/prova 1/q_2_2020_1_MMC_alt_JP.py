n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
i = 2
MMC = 0
maiorNumero = n2
if n1 > n2:
    maiorNumero = n1

while MMC == 0 and i < maiorNumero:
    if i % n1 == 0 and i % n2 == 0:
        MMC = i
    i += 1

if MMC == 0:
    MMC = n1 * n2

print(MMC)