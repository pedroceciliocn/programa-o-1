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
N = 0
while True:
    codigo = int(input("Código do curso: "))
    if codigo <= 0:
        break
    nome = input("Nome do curso: ")
    centro = int(input("Centro do curso: "))
    if centro <= 0:
        break
    tabela[codigo] = (nome, centro)
    N += 1
print(f"Tabela com {N} cursos lidas corretamente.")
print(f"Tabela->{tabela}")

centro = int(input("Dê um centro (0 ou negativo pra parar): "))
while centro > 0:
    for codigo, value in tabela.items():
        if centro in value:
            print(f"Centro {value[1]} tem o curso {value[0]} de código {codigo}")

        # nome, centro = tabela[codigo]
        # print(f"Curso {nome} de codigo {codigo} é do centro {centro}")
    # for codigo, value in tabela.items():
    #     if value[1] == centro:
    #         print(f"Centro {value[1]} tem o curso {value[0]} de código {codigo}")
    centro = int(input("Dê um centro (0 ou negativo pra parar): "))
print("Fim do programa.") 