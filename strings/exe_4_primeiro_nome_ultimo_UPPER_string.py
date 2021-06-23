"""
.upper() até o primeiro espaço e depois .upper() iniciando da última letra até o primeiro espaço

.rfind() encontra começando da direita


s = "On the other hand, you have different fingers."
s. find("hand")
13  #The results tell us that “hand” begins at the 13th position in the sequence.

But if we want to find the second “o” we need to specify a range.
s.find("o", 8)
20

This begins searching at the 8th element and finds “o” at 20. You can also specificy an end to the range, and, like
slicing, we can do so backwards:
s.find("e", 20, -5)
26
"""

nome = input("Dê seu nome completo: ")

i_fim_primeiro = nome.find(" ") #indice do primeiro espaço
i_inicio_ultimo = nome.rfind(" ") #indice do primeiro espaço comecando da direita

primeiro = nome[0:i_fim_primeiro].upper()
ultimo = nome[i_inicio_ultimo + 1:].upper()
meio = nome[i_fim_primeiro + 1:i_inicio_ultimo].lower().title()
print(f"{primeiro} {meio} {ultimo}")
