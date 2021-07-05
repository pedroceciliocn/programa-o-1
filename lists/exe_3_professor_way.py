"""Ler as notas de N alunos (N é informado pelo
usuário antes), calcular e imprimir a média das
notas e depois imprimir as notas que sejam
maiores do que a média calculada."""
N = int(input("Dê o N (número de alunos): "))
while N <= 0:
    N = int(input("Dê o N (maior que 0): "))

notas = [0]*N
soma = 0
for i in range(N):
    nota = float(input(f"Nota do aluno {i}: "))
    notas[i] = nota
    soma += notas[i]
media = soma / N
print(f"Média: {media:.2f}")
print(f"Notas maiores que a Média {media:.2f}: ")
for i in range(N):
    if notas[i] > media:
        print(f"Nota {notas[i]} do aluno {i}")


