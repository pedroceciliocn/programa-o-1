def ler_arquivo(nome='/home/pedro/Documentos/programação_1/arquivos e exceções/profissoes.txt'):
    dict = {}
    try:
        with open(nome, 'r') as arq_lido:
            for linha in arq_lido:
                lst = linha.split()
                dict[int(lst[0])] = ' '.join(lst[1:])
    except FileNotFoundError:
        print(f"Arquivo/caminho {nome} não encontrado.")

    return dict

dict = ler_arquivo()
fim = False

while not fim:
    try:
        codigo = int(input("Digite um código positivo (zero ou negativo para): "))
        while codigo > 0:
            if codigo in dict:
                print(f"O código {codigo} corresponde à profissão de {dict[codigo]}")
            else:
                print("Profissão inexistente.")
                with open('cod_invalidos.txt', 'a') as arq_invalido:
                    arq_invalido.write(f"{codigo}\n")

            codigo = int(input("Digite um código positivo (zero ou negativo para): "))
    except ValueError:
        print("O código deve ser um número inteiro.")
    except PermissionError:
        print("Sem permissão de criação de arquivo")
    else:
        fim = True


    