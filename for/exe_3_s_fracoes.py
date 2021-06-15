n = -1

s = 0
for d in range(1, 51):
    n += 2
    s += (n/d)
    print(f"{n}/{d} +")
print(f"S = {s:.2f}")
