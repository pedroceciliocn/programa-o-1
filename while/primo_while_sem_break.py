numero = int(input("De um numero inteiro e direi se ele é primo.\n"))

if numero == 0 or numero == 1:
    print("0 ou 1 não são primos por motivos específicos.")
else:
    if numero == 2:
        print("2 é primo (o unico primo par).")
    elif numero % 2 == 0:
        print(f"O numero {numero} não é primo, pois o resto da divisao por 2 deu 0\n e o 2 é o único par primo.")
    else:
        x = 3
        while x < numero and numero % x != 0:
            x += 2
        if x == numero:
            print(f"{numero} é primo.")
        else:
            print(f"{numero} não é primo, pq ele é divisível por {x}, que é ímpar.")