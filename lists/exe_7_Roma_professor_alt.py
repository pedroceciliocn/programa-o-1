"""
Fazer um programa Python para:
– Ler um número inteiro positivo N digitado pelo usuário -
o programa deve verificar se o valor de N é válido.
– Depois, ler N números inteiros positivos (0 < x < 4000)
e, para cada um deles, imprimir a sua representação
em algarismos romanos.
– Construir o resultado (valor em algarismos romanos)
usando um String.
– OBS. Lembre que os valores dos algarismos romanos
são: I=1, V=5, X=10, L=50, C=100, D=500, e M=1000,
e que IV=4, IX=9, XL=40, XC=90, CD=400 e CM=900.
"""
tab = [(1000,'M'),(900,'CM'),(500,'D'), (400,'CD'), (100,'C'),
       (90,'XC'), (50,'L'), (40,'XL'), (10,'X'), (9,'IX'),
       (5,'V'), (4,'IV'), (1,'I')]

num = int(input('Digite um número: '))
while (num < 1) or (num > 3999) :
    num = int(input('Digite um número: '))

aux = num
res = ''

for i in tab : 
    while aux >= tab[0] :
        res = res + tab[1]
        aux = aux - tab[0]

print(num, '=', res)