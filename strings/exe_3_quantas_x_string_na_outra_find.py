s_1 = input("Dê a primeira string: ")
s_2 = input("Dê a segunda string: ")

contador = 0
i = 0

if len(s_1) > len(s_2):
    s_2, s_1 = s_1, s_2

while True:
    contido = s_2.find(s_1, i)
    if contido == -1:
        break
    else:
        contador += 1
        i = contido + 1
print(f"A string aparece {contador} vezes na outra.")
