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
# leitura
tab = {}
n = 0

codigo_curso = int(input("Código do curso (0 para parar): "))
while codigo_curso < 1:
    codigo_curso = int(input("Inválido. Digite novamente o código do curso: "))

while codigo_curso != 0:
    nome_curso = input("Nome do curso: ")
    codigo_centro = int(input("Código do centro: "))
    while codigo_centro < 1:
        codigo_centro = int(input("Inválido. Digite novamente o código do centro: "))
    tab[codigo_curso] = (nome_curso, codigo_centro)
    n += 1

    codigo_curso = int(input("Código do curso (0 para parar): "))
    while codigo_curso < 0 or codigo_curso in tab:
        codigo_curso = int(input("Inválido. Digite novamente o código do curso: "))

print(f"Tabela com {n} cursos lida corretamente.\n {tab}")

#consulta
codigo_centro = int(input("Código do centro para pesquisar: "))
while codigo_centro < 1:
    codigo_centro = int(input("Inválido. Digite novamente o código do centro a ser pesquisado: "))

while codigo_centro > 0:
    qtd = 0
    print(f"Cursos do centro {codigo_centro}: ")
    for chave in tab:
        if codigo_centro == tab[chave][1]:
            qtd += 1
            print(f"   {chave}: {tab[chave][0]}")
    if qtd == 0:
        print(f"Nenhum curso encontrado no centro {codigo_centro}")        
    codigo_centro = int(input("Código do centro para pesquisar: "))
print("Fim do programa.")
