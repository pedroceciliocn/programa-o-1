def leitura(profissões):
    codigo = int(input("Digite o código da profissão: "))
    while codigo <= 0:
        codigo = int(input("Digite o código da profissão (maior que 0): "))
    nome = input("Digite o nome da profissão: ")
    área = input("Digite a área da profissão: ")
    
    profissões[codigo] = (nome, área)


N = int(input("Digite a quantidade de profissões: "))
while N <= 0:
    N = int(input("Digite a quantidade de profissões (maior que 0): "))

prof = {}
for i in range(N):
    leitura(prof)

codigo = int(input("Digite o código para ser pesquisado: "))
while codigo > 0:
    if codigo in prof: #dic mais eficiente em busca, lista em inserção
        nome_profissão = prof[codigo][0]
        area_profissão = prof[codigo][1]
        print(f"Nome da profissão: {nome_profissão}\nÁrea: {area_profissão}")
    else:  
        print("Profissão não encontrada")   

    codigo = int(input("Digite o código para ser pesquisado (negativo para): "))