# – Ler um arquivo do Detran onde cada registro contém as
# seguintes informações: placa, marca, modelo e ano de
# cada veículo, além do CPF do proprietário. O nome
# físico do arquivo será fornecido pelo usuário.
# – Gravar em um outro arquivo com nome externo
# “veicVelhos.txt” a placa e ano do veículo e o CPF dos
# proprietários de todos os veículos que sejam do ano
# 2000 ou mais velhos.
# – Informar no final ao usuário o número de veículos
# velhos gravados no arquivo.

fim = False
tot_veic_velhos = 0
while not fim:
    try:
        nome_arquivo = input("Digite o nome/caminho do arquivo: ")
        registros = open(nome_arquivo, 'r')
        veic_velhos = open('veicVelhos.txt', 'w')
        with registros, veic_velhos:
            for reg in registros:
                placa, marca, modelo, ano, cpf = reg.split()
                if int(ano) <= 2000:
                    veic_velhos.write(f'{placa} {ano} {cpf}\n')
                    tot_veic_velhos += 1
    except FileNotFoundError:
        print("Arquivo informado pelo usuário não encontrado. Digite um nome válido.")
    else:
        print(f"Tarefa realizada com sucesso. Número de veículos velhos armazenados: {tot_veic_velhos}")
        fim = True