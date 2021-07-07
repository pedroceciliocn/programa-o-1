"""
Fazer um programa para:
- ler uma tabela de cursos, onde:
    cada curso é formado por um código (número positivo), 
    um nome (string), e o centro a que pertence  (número positivo)
- depois o usuário fornecerá uma lista de códigos de centro para que
o programa imprima o código e nome de todos os cursos associados a cada
centro digitado.
- se o código do centro não existir na tabela, mostrar a mensagem
"Nenhum curso encontrado" e continuar.
- o programa pára com a digitação de um código de centro inválido
(negativo ou zero).
"""

tabela = {}
n = 0
while True:
    codigo = int(input("Código do curso: "))
    if codigo <= 0:
        break
    nome = input("Nome do curso: ")
    centro = int(input("Centro do curso: "))
    if centro <= 0:
        break
    tabela[codigo] = (nome, centro)
    n += 1
print (f'Tabela com {n} cursos foi lida corretamente.')
print(f"Tabela->{tabela}")

# codigos_centros = []
# while True:
#     codigo_centro = int(input("De um codigo de centro (0 ou negativo pra parar): "))
#     if codigo_centro <= 0:
#         print("Centro inválido")
#         break
#     else:
#         codigos_centros.append(codigo_centro)

while True:
    codigo_centro = int(input("De um codigo de centro (0 ou negativo pra parar): "))
    if codigo_centro <= 0:
        print("Centro inválido")
        break
    else:
        for i in tabela:
            if tabela[i][1] == codigo_centro:
                print(f"{i}: {tabela[i][0].title()}")

# for i in tabela:
#     # print(i, tabela[i])
#     if tabela[i][1] in codigos_centros:
#         print(tabela[i][1])

# while True:
#     codigo_centro = int(input("De um codigo de centro (0 ou negativo pra parar): "))
#     if codigo_centro <= 0:
#         print("Centro inválido")
#         break
#     else:
#         codigos_centros.append(codigo_centro)
#         for value in tabela.values():
#             if value[1] in codigos_centros:
#                 print(f"Centro {value[1]} e curso {value[0]}")
# for value in tabela.values():
#     if value[1] in codigos_centros:
#         print(f"O curso {value[0]} do centro {value[1]}")
#     else:
#         print("Nenhum curso encontrado")

# for key in sorted(tabela.keys()): # printando somente as keys ordenadas
#     print(key)

# for value in tabela.values(): # printando values
#     print(value) 

# for key, value in tabela.items(): # printando keys e values
#     print(key, value)

# contido = tabela.get(codigo, 'Codigo nao encontrado')
# print(contido)