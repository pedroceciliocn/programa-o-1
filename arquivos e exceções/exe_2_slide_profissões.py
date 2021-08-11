"""
Fazer um programa para:
    – Ler um arquivo com profissões, onde cada profissão é
    formada por um código (positivo) e um nome (String), uma
    profissão por linha.
    – Receber do usuário uma lista de códigos para que o
    programa informe o nome de cada profissão.
    – Se o código da profissão não existir no arquivo, mostrar a
    mensagem “Profissão Inexistente”, gravar em outro arquivo
    estes códigos de profissões, e continuar.
    – O programa pára com a digitação de um código inválido
    (negativo ou zero).
"""

fim = False

while not fim:
    try:
        nome_arquivo = input("Digite o nome/caminho do arquivo: ")
        # profissões = open(nome_arquivo, 'r')
        # codigos_inexistentes = open('/home/pedro/Documentos/programação_1/arquivos e exceções/codigos.inexistentes.txt', 'w')

        # lista = []
        # numero = int(input("Dê um código de profissão: "))
        # while numero > 0:
        #     lista.append(numero)
        #     numero = int(input("Dê mais um código de profissão: (0 ou negativo para)"))

        with open("codigos.inexistentes.txt", "w") as inexistentes:
            with open(nome_arquivo) as profissoes:
                for profissao in profissoes:
                    codigo = profissao[0:3] 
                    nome = profissao[4:]
                    numero = int(input("Dê o codigo de uma profissão: "))
                    if numero > 0:
                        if str(numero) != codigo:
                            inexistentes.write(str(numero))
                        elif str(numero):
                            print(f"{codigo} {profissao}")
                    else:
                        fim = True
        
    except FileNotFoundError:
        print("Arquivo informado pelo usuário não encontrado. Digite um nome válido.")
    else:
        fim = True  