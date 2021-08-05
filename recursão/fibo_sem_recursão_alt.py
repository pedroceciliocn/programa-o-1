def fibonacci(n):
    x = -1
    y = 1
    res = 0
    while n > 0:
        res = x + y
        x = y
        y = res
        n -= 1
    return res

num = int(input("Dê o termo da sequência de Fibonacci: "))
while num > 0:
    print(f"O termo {num} da sequência é: {fibonacci(num)}")
    num = int(input("Dê o termo da sequência de Fibonacci: "))

        