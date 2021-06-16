"""
Calcular o valor de S com N termos, onde N é
informado pelo usuário e S é:
    S = 2/500 - 5/490 + 2/480 - 5/470 + ...
"""

N = int(input("Digite o N (numero de termos): "))

d = 500
s = 0
for i in range(1, N+1):
    if i % 2 == 0:
        s += -5/d
        print(f"- 5/{d}")
    else:
        s += 2/d
        print(f"+ 2/{d}")
    d -= 10    
print("____________")
print(f"S = {s:.4f}")
