"""
Fazer um programa para:
    - Ler números inteiros positivos digitados pelo usuário.
        A leitura para quando um número negativo for digitado.
    - Imprimir, para cada um deles, o termo equivalente na
    sequência de Fibonacci.
    - Os números da sequência de Fibonacci são:
        0, 1, 1, 2, 3, 5, 8, 13, ... Note que a partir do terceiro
        termo, cada termo é a soma dos 2 termos anteriores.
    - Usar uma subrotina que recebe o número do termo
    como parâmetro e retorna o seu valor.
        implementá-la nas versões recursivas e não recursiva."""

# fibo recursivo
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(0)) # fibonacci com n = 0
# print(fibonacci(1)) # fibonacci com n = 1
# print(fibonacci(4)) # fibonacci com n = 4

num = int(input("Dê o termo da sequência de Fibonacci: "))
while num >= 0:
    print(f"O termo {num} da sequência é: {fibonacci(num)}")
    num = int(input("Dê o termo da sequência de Fibonacci: "))


