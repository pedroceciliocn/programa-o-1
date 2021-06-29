"""Ler as notas de N alunos (N é informado pelo
usuário antes), calcular e imprimir a média das
notas e depois imprimir as notas que sejam
maiores do que a média calculada."""
N = int(input("Dê o N (número de alunos): "))
while N <= 0:
    N = int(input("Dê o N (maior que 0): "))

notas = []
soma = 0
for x in range(N):
    nota = float(input(f"Nota do aluno {x}: "))
    notas.append(nota)
    soma += notas[x]
media = soma / N

maiores = []
for elemento in notas:
    if elemento > media:
        maiores.append(elemento)

print(f"Notas: {notas}")
print(f"Média: {media:5.2f}")
print(f"Notas maiores que a média: {maiores}")