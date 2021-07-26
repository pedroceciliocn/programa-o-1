# fibo sem recursão
def fibonacci(n):
    primeiro = 0
    segundo = 1
    aux = 0
    while n > 0:
        aux = primeiro
        primeiro = segundo
        segundo += aux
        n -= 1
    return primeiro

num = int(input("Dê o termo da sequência de Fibonacci: "))
while num >= 0:
    print(f"O termo {num} da sequência é: {fibonacci(num)}")
    num = int(input("Dê o termo da sequência de Fibonacci: "))



# def fibonacci(n):
#     primeiro = 0
#     segundo = 1
#     while n > 0:
#         primeiro, segundo = segundo, segundo + primeiro
#         n -= 1
#     return primeiro