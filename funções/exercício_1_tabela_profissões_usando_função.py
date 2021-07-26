def leitura():
    codigo = int(input("Digite o código da profissão: "))
    while codigo <= 0:
        codigo = int(input("Digite o código da profissão (maior que 0): "))
    nome = input("Digite o nome da profissão: ")
    área = input("Digite a área da profissão: ")

    return codigo, nome, área

N = int(input("Digite a quantidade de profissões: "))
while N <= 0:
    N = int(input("Digite a quantidade de profissões (maior que 0): "))

prof = [(0, "", "")] * N

for i in range(N):
    prof[i] = leitura()

codigo = int(input("Digite o código para ser pesquisado: "))
while codigo > 0:
    pos = 0
    while pos < N and prof[pos][0] != codigo: #cuidado com a ordem do and
        pos += 1
    
    if pos == N:
        print("Profissão não encontrada")
    else:
        nome_profissão = prof[pos][1]
        area_profissão = prof[pos][2]
        print(f"Nome da profissão: {nome_profissão}\nÁrea: {area_profissão}")

    codigo = int(input("Digite o código para ser pesquisado (negativo para): "))