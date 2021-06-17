"""Dada uma sequencia de n notas, cada uma com um peso p,
calcule a media ponderada dessas notas
"""
n = int(input("Dê a quantidade de notas: "))
soma = 0
peso = 0
pesos = 0
media = 0
for x in range(n):
    if n <= 0:
        print("Inválido!")
    else:
        nota = float(input(f"Dê o {x+1}º nota: "))
        peso = float(input(f"Dê o peso da {x+1}ª nota: "))
        soma += nota * peso
        pesos += peso
if soma > 0:
    media = soma / pesos
    print(f"A média ponderada das {n} notas foi de {media:<.2f}.")
else:
    print("Seu chibata.")
