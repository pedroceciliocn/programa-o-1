s_1 = input("Dê a primeira string: ")
s_2 = input("Dê a segunda string: ")

if len(s_1) > len(s_2):
    s_2, s_1 = s_1, s_2
contador = 0
for i in range(0, len(s_2) - len(s_1) + 1):
    if s_2[i:i+len(s_1)] == s_1:
        contador += 1
print(f"A string aparece {contador} vezes na outra.")

#ta dando problema com strings repetidas seguidamente


