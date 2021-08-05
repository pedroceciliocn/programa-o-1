def fibR(n, t1 = 1, res = 0):
    if n > 1:
        res = fibR(n - 1, res, t1 + res)
    return res

num = int(input("Dê o termo da sequência de Fibonacci: "))
while num < 1:
    num = int(input("Dê o termo POSITIVO da sequência de Fibonacci: "))

while num >= 0:
    r = fibR(num)
    print(f"O termo {num} da sequência é: {r}")
    num = int(input("Dê um termo da sequência de Fibonacci: "))
    while num == 0:
        num = int(input("Dê um termo POSITIVO da sequência de Fibonacci: "))