"""
Q3 – Faça uma subrotina Python do tipo Procedimento chamada MelhoresClientes para:
    
    (a) ler um arquivo texto, cujo nome externo é formado a partir do nome de uma empresa,
    recebido como parâmetro, seguido da extensão '.txt'. O arquivo conterá as informações dos
    clientes do programa de fidelidade desta empresa, a saber: matrícula (inteiro com 5 dígitos),
    sexo (1=masculino ou 2=feminino), número de pontos (inteiro com 7 dígitos), e nome do
    cliente (string com 35 posições). Arquivo exemplo será fornecido juntamente com a questão.
    
    (b) Gravar um arquivo, cujo nome externo é 'Melhores' concatenado após o nome da empresa,
    seguido da extensão '.txt', contendo somente a matrícula e o total de pontos (um cliente por
    linha) dos clientes com pontuação acima de um dado valor recebido como segundo parâmetro
    na subrotina. Ou seja, este procedimento deve ter 2 parâmetros.
    
    (c) No final, o procedimento deve imprimir (na tela do terminal) um resumo das informações
    gravadas no arquivo contendo o nome da empresa, o número de registros gravados no arquivo
    e a média das pontuações destes melhores clientes.

Faça também um programa principal que leia o nome da empresa e o total de pontos a ser
considerado na escolha dos melhores clientes de N empresas, com N informado no início pelo
usuário, e faça uso do procedimento MelhoresClientes para cada uma delas. Caso ocorra erro
no arquivo de alguma das empresas, o seu programa deve informar o usuário e desconsiderar
esta empresa, possivelmente continuando a executar com outras empresas.
"""

def MelhoresClientes(nome_empresa, pontuação):
    soma = 0
    cont = 0
    empresa = open(f'{nome_empresa}.txt', 'r')
    Melhores = open(f'{nome_empresa}Melhores.txt', 'w')
    with empresa, Melhores:
        for clientes in empresa:
            matricula = clientes[0:5] 
            sexo = clientes[6:7]
            pontos = clientes[8:15]
            nome = clientes[16:51]
    
            if int(pontos) > int(pontuação):
                Melhores.write(f'{matricula} {pontos}\n')
                cont += 1
                soma += int(pontos)
        print(f"A média de pontuação dos {cont} melhores clientes (que tem pontuação superior à informada) da empresa '{nome_empresa}' foi de {soma/cont:.2f} pontos")
        


# MelhoresClientes('P1SI-p2-2020-1-Q3-Arquivo', 60000)
# MelhoresClientes('Nobre', 10000)


# MARROMENO ERRADO
# N = int(input("Dê o numero N de empresas: "))
# while N < 0:
#     N = int(input("Dê o numero N de empresas: "))

# fim = False
# while not fim:
#     try:
#         while N > 0:
#             nome_empresa = input('Dê o nome da empresa: ')
#             pontuação = int(input('Dê a pontuação a ser considerada: '))
#             while pontuação > 999999 or pontuação < 0:
#                 pontuação = int(input('Dê a pontuação a ser considerada (com menos de 6 dígitos e positiva): '))
#             MelhoresClientes(nome_empresa, pontuação)
#             N -= 1
#     except FileNotFoundError:
#         print(f"Arquivo '{nome_empresa}.txt' informado pelo usuário não encontrado. Digite um nome válido.")
#     except PermissionError:
#         print("Sem permissão de criação de arquivo")
#     except ZeroDivisionError:
#         print(f"Não tem cliente algum com pontuação maior que {pontuação}")
#     else:
#         fim = True

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

# fim = False
# while not fim:
#     while N > 0:
#         try:
#             nome_empresa = input('Dê o nome da empresa: ')
#             pontuação = int(input('Dê a pontuação a ser considerada: '))
#             while pontuação > 999999 or pontuação < 0:
#                 pontuação = int(input('Dê a pontuação a ser considerada (com menos de 6 dígitos e positiva): '))
#             MelhoresClientes(nome_empresa, pontuação)
#             N -= 1
#         except FileNotFoundError:
#             print(f"Arquivo '{nome_empresa}.txt' informado pelo usuário não encontrado. Digite um nome válido.")
#         except PermissionError:
#             print("Sem permissão de criação de arquivo")
#         except ZeroDivisionError:
#             print(f"Não tem cliente algum com pontuação maior que {pontuação}")
#         else:
#             fim = True


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
                print(f"Arquivo '{nome_empresa}.txt' informado não encontrado. Empresa desconsiderada! Digite um nome válido.")         
            except ZeroDivisionError:
                print(f"Não tem cliente algum com pontuação maior que {pontuação}")
            else:
                N -= 1
                fim = True
        
        




# ERRADO
# N = int(input("Dê o número N de empresas para verificação: "))

# erro = False
# for i in range(N):
#     try:
#         nome_empresa = input('Dê o nome da empresa: ')
#         pontuação = float(input('Dê a pontuação a ser considerada: '))
#     except:
#         erro = True
#     else:
#         MelhoresClientes(nome_empresa, pontuação)
#     while erro:
#         try:
#             nome_empresa = input(f"Arquivo '{nome_empresa}.txt' informado pelo usuário não encontrado. Digite um novo nome válido: ")
#             pontuação = float(input(f'Pontuação "{pontuação}" inválida. Dê uma nova pontuação a ser considerada: '))
#         except:
#             erro = True    
#         else:
#             MelhoresClientes(nome_empresa, pontuação)








