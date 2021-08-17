"""
2 – Faça um programa Python para:
    (a) ler um arquivo (nome externo 'clientes.arq'), contendo informações das pessoas que são
    clientes do programa de fidelidade da empresa: matric (inteiro com 5 dígitos), sexo (1=masc.
    ou 2=fem.), pontos (inteiro com 7 dígitos), e nome (string com 35 posições).
    
    (b) criar um arquivo (nome externo 'melhores.arq') contendo somente a matrícula e o total de
    pontos (um cliente por linha) com pontuação acima de um dado valor (informado antes pelo
    usuário).

    (c) No final, o programa deve imprimir (na tela do terminal) um resumo das informações
    gravadas no arquivo contendo o número de registros gravados no arquivo e a média das
    pontuações destes clientes.
"""

def MelhoresClientes(nome_empresa, pontuação):
    soma = 0
    n_registros = 0
    empresa = open(f'{nome_empresa}.txt', 'r')
    Melhores = open(f'melhores.{nome_empresa}.txt', 'w')
    with empresa, Melhores:
        for clientes in empresa:
            matric = int(clientes[0:5]) 
            sexo = clientes[6:7]
            pontos = int(clientes[8:15])
            nome = clientes[16:51]
    
            if pontos > pontuação:
                Melhores.write(f'{matric} {pontos}\n')
                n_registros += 1
                soma += pontos
        print(f"A média de pontuação dos {n_registros} melhores clientes (que tem pontuação superior à informada) da empresa '{nome_empresa}' foi de {soma/n_registros:.2f} pontos")

fim = False
while not fim:
    try:
        N = int(input("Dê o numero N de empresas: "))
        while N < 0:
            N = int(input("Dê o numero N de empresas: "))
    except ValueError:
        print("Digite um número inteiro!")
    else:
        fim = True

fim = False
while not fim:
    while N > 0:
        try:
            nome_empresa = input('Dê o nome da empresa: ')
            pontuação = int(input('Dê a pontuação a ser considerada: '))
            while pontuação > 999999 or pontuação < 0:
                pontuação = int(input('Dê a pontuação a ser considerada (com menos de 6 dígitos e positiva): '))
        except ValueError:
            print("Você deu uma string na pontuação! Dê um número.")
        else:    
            try:
                MelhoresClientes(nome_empresa, pontuação)
            except FileNotFoundError:
                print(f"Arquivo '{nome_empresa}.txt' informado não encontrado. Empresa desconsiderada!")         
            except ZeroDivisionError:
                print(f"Não tem cliente algum com pontuação maior que {pontuação}. Pontuação desconsiderada!")
            else:
                N -= 1
                fim = True