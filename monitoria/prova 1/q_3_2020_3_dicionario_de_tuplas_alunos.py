"""
Questão 3 – Faça um programa Python para ler uma tabela de alunos onde:
    • Cada aluno tem uma matrícula (int), um nome (string) e uma idade (int).
    • A leitura da tabela pára com uma matrícula que não seja positiva.
    • O usuário só pode digitar no máximo 200 alunos.
Depois o usuário informará um inteiro positivo N, seguido por uma série de N intervalos
de idades (idades mínima e máxima), e o programa deve imprimir, para cada intervalo
digitado pelo usuário, os dados dos alunos que se enquadram no intervalo, seguidos pelo
número de alunos do intervalo. Caso a idade mínima de algum intervalo seja maior do
que a idade máxima, o programa deve simplesmente imprimir uma mensagem de erro e
continuar
"""
# leitura
tab = {}
n = 0

matricula = int(input("Matrícula: "))
while matricula < 0:
    matricula = int(input("Inválido. Digite novamente a matrícula (negativo para parar): "))

while matricula > 0 and n <= 200: #incossistencia???
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    while idade < 1:
        idade = int(input("Inválido. Digite novamente a idade do aluno: "))
    tab[matricula] = (nome, idade)
    n += 1

    matricula = int(input("Matrícula (0 ou negativo para parar): "))
    while matricula in tab:
        matricula = int(input("Repetido. Digite novamente a matrícula do aluno (0 ou negativo para parar): "))

print(f"Tabela com {n} alunos lida corretamente.\n {tab}") #para conferir (dicionário de tuplas - podia ser de listas)

#consulta
N = int(input("Dê o N de intervalos a pesquisar: "))
while N < 1:
    N = int(input("Inválido. Dê o N de intervalos a pesquisar: "))

for i in range(N):
    min = int(input(f"Dê o {i+1}º intervalo mínimo de idade: "))
    while min < 0:
        min = int(input(f"Mínimo negativo! Dê o {i+1}º intervalo mínimo de idade: "))
    max = int(input(f"Dê o {i+1}º intervalo máximo de idade: "))
    while max < 0 or max < min:
        max = int(input(f"Errado! Dê o {i+1}º intervalo máximo de idade: "))
    else:
        qtd = 0
        print(f"Alunos na faixa {min}~{max} anos de idade: ")
        for matricula in tab:
            if min <= tab[matricula][1] and max >= tab[matricula][1]:
                qtd += 1
                print(f"Matrícula {matricula}: {tab[matricula][0].title()}, {tab[matricula][1]} anos")
        print(f"Total de alunos: {qtd}")
        if qtd == 0:
            print(f"Nenhum aluno encontrado na faixa {min}~{max} de idade")
            
            




# codigo_centro = int(input("Código do centro para pesquisar: "))
# while codigo_centro < 1:
#     codigo_centro = int(input("Inválido. Digite novamente o código do centro a ser pesquisado: "))

# while codigo_centro > 0:
#     qtd = 0
#     print(f"Cursos do centro {codigo_centro}: ")
#     for chave in tab:
#         if codigo_centro == tab[chave][1]:
#             qtd += 1
#             print(f"   {chave}: {tab[chave][0]}")
#     if qtd == 0:
#         print(f"Nenhum curso encontrado no centro {codigo_centro}")        
#     codigo_centro = int(input("Código do centro para pesquisar: "))
# print("Fim do programa.")
