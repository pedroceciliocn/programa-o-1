"""
Fazer um programa em Python para:
– Ler uma tabela com N profissões, onde
    • O valor de N é informado antes pelo usuário.
    • Cada profissão é formada por um código (número positivo) e
    um nome e uma área (ambos String). – Depois o usuário fornecerá
    uma lista de códigos para que o programa informe o nome/área 
    das profissões.
– Se o código da profissão não existir na tabela, mostrar
a mensagem “Profissão ... não existe na tabela.” e
continuar.
– O programa deve parar com a digitação de um código
inválido (negativo ou zero).
"""
N = int(input("Dê o numero N de profissoes da tabela: "))
while N <= 0:
    N = int(input("Dê o numero N de profissoes (maior que 0) da tabela: "))

tabela = {}
for i in range(N):
    codigo = int(input("Dê o código da profissão: "))
    while codigo <= 0:
        codigo = int(input("Dê o código da profissão (maior que 0): "))
    nome = input("Dê o nome da profissão: ")
    area = int(input("Dê a área da profissão: "))
    tabela[codigo] = (nome, area) #dicionario de tuplas
print(f"Tabela com {N} profissões lidas corretamente.")
print(f"Tabela->{tabela}")

codigo = int(input("De um codigo de profissao (0 ou negativo pra parar): "))
while codigo > 0:
    if codigo in tabela:
        nome, area = tabela[codigo]
        print(f"Profissão {codigo} é {nome} e sua área é {area}")
    else:
        print(f"Profissão {codigo} não encontrada")
    codigo = int(input("De um codigo de profissao (0 ou negativo pra parar): "))
print("Fim do programa.") 

