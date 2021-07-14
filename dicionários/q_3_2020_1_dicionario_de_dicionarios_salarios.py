"""
Faça um programa Python para ler uma tabela de pessoas onde: 
• Cada pessoa tem um cpf (long), um nome (String) e um salário (float). 
• A leitura da tabela pára com um cpf que não seja positivo. 
• O usuário só pode digitar no máximo 300 pessoas. 
 Depois o usuário informará um intervalo de salários (fechado), ou seja, os limites inferior e 
superior do intervalo. Ambos devem ser positivos, mas o limite inferior pode ser zero. Além 
disto, o limite inferior do intervalo deve ser menor do que o limite superior. Caso alguma 
restrição seja violada, o programa deve informar ao usuário e pedir os dados novamentre. 
 De posse de um intervalo correto, o seu programa deve imprimir os dados das pessoas que se 
enquadram no intervalo, seguidos pelo número de pessoas do intervalo, pelo maior salário e 
pela média dos salários destas pessoas. O seu programa deve informar ainda quantas pessoas 
têm salários maiores do que o limite superior do intervalo. 
"""
continuar = True
quantidade_pessoas = 0
tabela = {}
soma = 0

while continuar and quantidade_pessoas <= 300:
    cpf = int(input("Digite o CPF: "))
    if cpf < 0:
        continuar = False
    else:
        nome = input("Digite o nome: ")
        salario = float(input("Digite o salário: "))
        tabela[cpf] = {'nome': nome, 'salário': salario}
        quantidade_pessoas += 1
print(f"Leitura concluída \n{tabela}") # dicionario de dicionarios

#intervalos = int(input("Digite o número de intervalos: "))
continuar = True
while continuar:
    quantidade_maior_que_superior = 0
    limite_inferior = int(input('Digite o limite inferior: '))
    limite_superior = int(input('Digite o limite superior: '))
    if limite_superior < limite_inferior:
        print("O limite superior deve ser maior que o inferior!")
    else:
        contador = 0
        maior = 0
        soma = 0
        for cpf in tabela.keys():
            pessoa = tabela[cpf]
            if pessoa['salário'] >= limite_inferior and pessoa['salário'] <= limite_superior:
                contador += 1
                if pessoa['salário'] > maior:
                    maior = pessoa['salário']
                print(f"CPF: {cpf}, nome: {pessoa['nome']}, salário: {pessoa['salário']}")
                soma += pessoa['salário']
            if pessoa['salário'] > limite_superior:
                quantidade_maior_que_superior += 1

        continuar = False
        print(f'Existem {contador} pessoas no intervalo R$ {limite_inferior:.2f} ~ R$ {limite_superior:.2f}')
        print(f"O maior salário nessa faixa é de R$ {maior:.2f}")
        print(f"A média de salários nessa faixa é de R$ {soma/contador:.2f}")
        print(f"Existem {quantidade_maior_que_superior} pessoas com salário maior que R$ {limite_superior:.2f}")
