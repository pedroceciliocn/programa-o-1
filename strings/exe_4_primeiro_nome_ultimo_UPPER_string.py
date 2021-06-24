"""
.upper() até o primeiro espaço e depois .upper() iniciando da última letra até o primeiro espaço

.rfind() encontra começando da direita
"""
nome = input("Dê seu nome completo: ").strip()

i_fim_primeiro = nome.find(" ") #indice do primeiro espaço
i_inicio_ultimo = nome.rfind(" ") #indice do primeiro espaço comecando da direita

primeiro = nome[:i_fim_primeiro].upper()
ultimo = nome[i_inicio_ultimo + 1:].upper()
meio = nome[i_fim_primeiro + 1:i_inicio_ultimo].lower().title()
print(f"{primeiro} {meio} {ultimo}")
