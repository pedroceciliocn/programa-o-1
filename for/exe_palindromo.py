s = input("Digite o número a verificar, sem espaços:")
i = 0
fim = len(s)-1  # posição do último caracter da string
while fim > i and s[i] == s[fim]:
    fim = fim - 1
    i = i + 1
if s[i] == s[fim]:
    print(f"{s} é um palíndromo")
else:
    print(f"{s} não é um palíndromo")
