"""
Calcular o valor de S, onde S é:
    S = 1 + 3/2 + 5/3 + 7/4 + ... + 99/50
"""
n = -1

s = 0
for d in range(1, 51):
    n += 2
    s += (n/d)
    print(f"{n}/{d} +")
print(f"S = {s:.2f}")
