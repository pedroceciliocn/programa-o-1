"""
Ler um número inteiro e dizer se ele é primo ou não.
dividindo o numero por todos os impares até ele e também
o dividindo por 2, se um dos restos for 0, o numero não
é primo. 0 e 1 não são primos e 2 é o unico par primo.
"""
numero = int(input("De um numero inteiro e direi se ele é primo.\n"))
if numero == 0 or numero == 1:
    print("0 ou 1 não são primos por motivos específicos.")
else:
    if numero == 2:
        print("2 é primo (o único primo par).")
    elif numero % 2 == 0:
        print(f"O numero {numero} não é primo, pois o resto da divisao por 2 deu 0\ne o 2 é o único par primo.")
    else:
        for x in range(3, numero+1, 2):
            if numero % x == 0:
                pass
        if x == numero:
            print(f"{numero} é primo.")
        else:
            print(f"{numero} não é primo, pq ele é divisível por {x}, que é ímpar.")
