"""
Calcular o valor de S, onde S é:
    S = 1 + 3/2 + 5/3 + 7/4 + ... + 99/50
"""
numerador = -1
s = 0
denominador = 1
while denominador <= 50:
    numerador += 2
    s += (numerador/denominador)
    print(f"{numerador}/{denominador} +")
    denominador += 1
print(f"S = {s:.2f}")