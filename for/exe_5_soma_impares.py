n_1 = int(input("De o primeiro valor do intervalo: "))
n_2 = int(input("De o segundo valor do intervalo: "))
s = 0
if n_1 > n_2:
    n_1, n_2 = n_2, n_1
for i in range(n_1, n_2 + 1):
    if i % 2 != 0:
        s += i
        print(f"+    {s}")
print("------")
print(f"s =  {s}")
        
