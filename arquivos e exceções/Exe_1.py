"""
Exercício
Considere um arquivo texto com nome externo  ́discip.old ́, contendo informações de disciplinas
(Código com 5 posições, nome com 35 posições e créditos com 2 posições), uma disciplina por
linha. Faça um programa Python para criar um segundo arquivo com nome externo  ́discip.new ́
contendo informações das mesmas disciplinas, mas com as seguintes modificações:
(a) As disciplinas cujos códigos são IF125 e IF380 devem ser excluídas, i.e., não devem ser
gravadas no novo arquivo.
(b) Os números de créditos das disciplinas cujos códigos começam por MA devem ser
alterados para 5.
(c) O novo arquivo terá um campo a mais (carga horária, com 3 posições) cujo valor deve ser
o número de créditos da disciplina multiplicado por 15.
No final o seu programa deve imprimir o número de disciplinas de cada arquivo e também o
número de disciplinas que tiveram seus números de créditos alterados.
"""
# fim = False
# total_discip_velhas = 0
# total_discip_novas = 0
# total_codigo_alterado = 0
#
# while not fim:
#     try:
#         nome_arquivo = input("Digite o nome/caminho do arquivo: ")
#         disciplinas = open(nome_arquivo, 'r')
#         discipnew = open('/home/pedro/Documentos/programação_1/arquivos e exceções/discip.new.txt', 'w')
#         # with open("discip.new.txt", "w") as discpnew:
#         #     with open(nome_arquivo) as disciplinas:
#         with disciplinas, discipnew:
#             for disciplina in disciplinas:
#                 código = disciplina[0:5]
#                 nome = disciplina[6:41]
#                 créditos = disciplina[42:44]
#                 if código.startswith('MA'):
#                     créditos = "5"
#                     total_codigo_alterado += 1
#                 if código == "IF125" or código == "IF380":
#                     discipnew.write('')
#                 else:
#                     discipnew.write(f'{código} {nome} {créditos}\n')
#                     total_discip_novas += 1
#
#                 total_discip_velhas += 1
#     except FileNotFoundError:
#         print("Arquivo informado pelo usuário não encontrado. Digite um nome válido.")
#     else:
#         print(f"Tarefa realizada com sucesso. Número de disciplinas velhas armazenadas: {total_discip_velhas}")
#         print(f"Número de disciplinas novas armazenadas: {total_discip_novas}")
#         print(f"Número de disciplinas com créditos alterados: {total_codigo_alterado}")
#         fim = True        
            



### ALTERNATIVA ########################################################################
# fim = False
# total_discip_velhas = 0
# total_discip_novas = 0
# total_codigo_alterado = 0

# while not fim:
#     try:
#         nome_arquivo = input("Digite o nome/caminho do arquivo: ")
#         # disciplinas = open(nome_arquivo, 'r')
#         # discipnew = open('/home/pedro/Documentos/programação_1/arquivos e exceções/discip.new.txt', 'w')
#         with open("discip.new.txt", "w") as discipnew:
#             with open(nome_arquivo) as disciplinas:
#                 for disciplina in disciplinas:
#                     código = disciplina[0:5]
#                     nome = disciplina[6:41]
#                     créditos = disciplina[42:44]
#                     carga = disciplina[45:47]
#                     if código.startswith('MA'):
#                         créditos = "5"
#                         total_codigo_alterado += 1
#                     if código == "IF125" or código == "IF380":
#                         discipnew.write('')
#                     else:
#                         carga = f'\t{str(int(créditos) * 15)}'
#                         discipnew.write(f'{código} {nome} {créditos}' + carga + f'\n') #talvez errado 
#                         total_discip_novas += 1

#                     total_discip_velhas += 1
#     except FileNotFoundError:
#         print("Arquivo informado pelo usuário não encontrado. Digite um nome válido.")
#     else:
#         print(f"Tarefa realizada com sucesso. Número de disciplinas velhas armazenadas: {total_discip_velhas}")
#         print(f"Número de disciplinas novas armazenadas: {total_discip_novas}")
#         print(f"Número de disciplinas com créditos alterados: {total_codigo_alterado}")
#         fim = True  





fim = False
total_discip_velhas = 0
total_discip_novas = 0
total_codigo_alterado = 0

while not fim:
    try:
        nome_arquivo = input("Digite o nome/caminho do arquivo: ")
        # disciplinas = open(nome_arquivo, 'r')
        # discipnew = open('/home/pedro/Documentos/programação_1/arquivos e exceções/discip.new.txt', 'w')
        with open("discip.new.txt", "w") as discipnew:
            with open(nome_arquivo) as disciplinas:
                for disciplina in disciplinas:
                    código = disciplina[0:5]
                    nome = disciplina[6:41]
                    créditos = disciplina[42:44]
                    carga = disciplina[45:47]
                    if código.startswith('MA'):
                        créditos = "5"
                        total_codigo_alterado += 1
                    if código == "IF125" or código == "IF380":
                        discipnew.write('')
                    else:
                        carga = str(int(créditos) * 15)
                        discipnew.write(f'{código} {nome} {créditos} \t{carga}\n') # ainda pode estar errado, pois a especificação de 3 posições não foi satisfeita
                        total_discip_novas += 1

                    total_discip_velhas += 1
    except FileNotFoundError:
        print("Arquivo informado pelo usuário não encontrado. Digite um nome válido.")
    else:
        print(f"Tarefa realizada com sucesso. Número de disciplinas velhas armazenadas: {total_discip_velhas}")
        print(f"Número de disciplinas novas armazenadas: {total_discip_novas}")
        print(f"Número de disciplinas com créditos alterados: {total_codigo_alterado}")
        fim = True  