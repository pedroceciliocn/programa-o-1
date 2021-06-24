s_1 = input("Dê a primeira string: ")
s_2 = input("Dê a segunda string: ")

if len(s_1) > len(s_2):
    s_2, s_1 = s_1, s_2

contador = 0

i = s_2.find(s_1)
while i != -1:
    contador += 1
    i = s_2.find(s_1, i + 1)
print(f"A string aparece {contador} vezes na outra.")