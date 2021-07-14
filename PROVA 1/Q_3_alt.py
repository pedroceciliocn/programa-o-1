"""
 Faça um programa Python para ler e armazenar uma tabela de disciplinas onde:
     Cada disciplina tem um código (string com exatamente 5 caracteres), seu nome (string),
sua carga horária (int, positivo) e seu número de créditos (int, positivo).
     A leitura da tabela pára com a digitação de ‘FIM’, ao invés de um código válido. 
     O usuário só pode digitar no máximo 500 disciplinas.
Depois o usuário informará um prefixo de código (string com menos de 5 caracteres) e o
programa deve imprimir os dados das disciplinas cujos códigos começam pelo prefixo
informado, bem como a média das cargas horárias dessas disciplinas. 
"""
tabela = {}
n = 0

codigo = input("Código da disciplina: ")
while len(codigo) != 5:
    codigo = input("Código inválido (deve ter 5 caracteres): ")

continuar = True
while continuar:
    nome = input("Nome da disciplina: ")
    carga = int(input("Carga horária: "))
    while carga < 1:
        carga = int(input("Inválida. Digite novamente a carga (maior que 0): "))
    creditos = int(input("Créditos: "))
    while creditos < 1:
        creditos = int(input("Inválido. Digite novamente os créditos (maior que 0): "))
    tabela[codigo] = (nome, carga, creditos)
    n += 1

    codigo = input("Código da disciplina ('FIM' PARA): ")
    while codigo in tabela or (len(codigo) !=5 and codigo != 'FIM'):
        codigo = input("Inválido ou repetido. Digite novamente o código: ")
    if codigo == 'FIM' or n > 500:
        continuar = False

print(f"Tabela com {n} disciplinas lida corretamente.\n {tabela}") #para conferir (dicionário de tuplas - podia ser de listas)

prefixo = input("Dê o prefixo de código da disciplina a ser buscada: ")
while len(prefixo) >= 5:
    prefixo = input("Inválido! Dê o prefixo de código com tamanho menor que 5: ")

soma = 0
qtd = 0

for codigo, valores in tabela.items():
    if codigo[0:len(prefixo)] == prefixo:
        qtd += 1
        soma += valores[1]
        print(f"Codigo: {codigo}; Disciplina: {valores[0]}; Carga Horária: {valores[1]}h; Créditos: {valores[2]}")

print(f"A média de carga horária das disciplinas encontradas foi de {soma/qtd:.2f}h")
