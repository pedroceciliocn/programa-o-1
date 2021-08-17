"""
2 – Considere um arquivo texto com nome externo ´discip.old´, contendo informações de
disciplinas (Código com 5 posições, nome com 35 posições e créditos com 2 posições), uma
disciplina por linha. Faça um programa Python para criar um segundo arquivo com nome
externo ´discip.new´ contendo informações das mesmas disciplinas, mas com as seguintes
modificações:
    (a) As disciplinas cujos códigos são IF125 e IF380 devem ser excluídas, i.e., não devem ser
    gravadas no novo arquivo.
    
    (b) Os números de créditos das disciplinas cujos códigos começam por MA devem ser
    alterados para 5.
    
    (c) O novo arquivo terá um campo a mais (carga horária, com 3 posições) cujo valor deve ser
    o número de créditos da disciplina multiplicado por 15.

No final o seu programa deve imprimir o número de disciplinas de cada arquivo e também o
número de disciplinas que tiveram seus números de créditos alterados.
"""

# MESMA QUESTÃO 'Exe_1.py' feita em sala, mas agora com a consistência feita fora
def Disciplinas(nome_arquivo):
    total_discip_velhas = 0
    total_discip_novas = 0
    total_codigo_alterado = 0
    disciplinas = open(f'{nome_arquivo}.txt', 'r')
    discipnew = open('new.discip.new.txt', 'w')
    with disciplinas, discipnew:
        for disciplina in disciplinas:
            código = disciplina[0:5]
            nome = disciplina[6:41]
            créditos = disciplina[42:44]
            if código != "IF125" and código != "IF380":
                if código[0:2] == ('MA'):
                    créditos = "5"
                    total_codigo_alterado += 1
                carga = int(créditos) * 15
                discipnew.write(f'{código} {nome} {créditos:2} {str(carga):3}\n')
                total_discip_novas += 1
            total_discip_velhas += 1
    print(f"Tarefa realizada com sucesso. Número de disciplinas velhas armazenadas: {total_discip_velhas}")
    print(f"Número de disciplinas novas armazenadas: {total_discip_novas}")
    print(f"Número de disciplinas com créditos alterados: {total_codigo_alterado}")  

fim = False
while not fim:
    try:
        nome_arquivo = input("Digite o nome/caminho do arquivo: ")
        Disciplinas(nome_arquivo)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}.txt' informado não encontrado. Chamada desconsiderada!")         
    else:
        fim = True