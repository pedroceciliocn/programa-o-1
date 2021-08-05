def fibR(n):
    if n == 1:
        res = 0
    else:
        if n == 2:
            res = 1
        else:
            res = fibR(n - 1) + fibR(n - 2)
    return res

num = int(input("Dê o termo da sequência de Fibonacci: "))
while num >= 0:
    print(f"O termo {num} da sequência é: {fibR(num)}")
    num = int(input("Dê o termo da sequência de Fibonacci: "))