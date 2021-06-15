f_1 = int(input("De o primeiro numero do intervalo em °F: "))
f_2 = int(input("De o segundo numero do intervalo em °F: "))
if f_1 > f_2:
    f_1, f_2 = f_2, f_1

for f in range(f_1, f_2 + 1):
    c = (f - 32)*(5/9)
    print(f"{f:2}°F = {c:.2f}ºC")

