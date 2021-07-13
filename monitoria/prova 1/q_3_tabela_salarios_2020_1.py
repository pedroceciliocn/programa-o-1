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
# leitura
tab = {}
n = 0
soma = 0

cpf = int(input("CPF: "))
while cpf < 0:
    cpf = int(input("Inválido. Digite novamente a CPF: "))

while cpf > 0 and n <= 300: 
    nome = input("Nome da pessoa: ")
    salario = float(input("Salário da pessoa: "))
    while salario < 0:
        salario = float(input("Inválido. Digite novamente o salario da pessoa: "))
    tab[cpf] = (nome, salario)
    n += 1

    cpf = int(input("CPF (negativo para parar): "))
    while cpf in tab or cpf < 0:
        cpf = int(input("CPF (negativo para parar): "))

print(f"Tabela com {n} pessoas lida corretamente.\n {tab}")

#consulta
N = int(input("Dê o N de intervalos a pesquisar: "))
while N < 1:
    N = int(input("Inválido. Dê o N de intervalos a pesquisar: "))

for i in range(N):
    min = float(input(f"Dê o {i+1}º intervalo mínimo de salário: "))
    if min < 0:
        min = float(input(f"Salário negativo! Dê o {i+1}º intervalo mínimo de salário: "))
    max = float(input(f"Dê o {i+1}º intervalo máximo de salário: "))
    if max < min:
        max = int(input(f"Errado! Dê o {i+1}º intervalo máximo de salário: "))
    else:
        qtd = 0
        maior_salario = 0
        qtd_maior_que_max = 0
        print(f"Pessoas na faixa R$ {min:.2f} ~ R$ {max:.2f} de salário: ")
        for cpf in tab:
            if min <= tab[cpf][1] and max >= tab[cpf][1]:
                qtd += 1
                if tab[cpf][1] > maior_salario:
                    maior_salario = tab[cpf][1]
                print(f"CPF {cpf}: {tab[cpf][0].title()}, R$ {tab[cpf][1]:.2f} de salário")
                soma += tab[cpf][1]
            if tab[cpf][1] > max:
                qtd_maior_que_max += 1
        
        if qtd == 0:
            print(f"Nenhuma pessoa encontrada na faixa R$ {min:.2f} ~ R${max:.2f} de salário")
        else:
            print(f"Total de pessoas na faixa R$ {min:.2f} ~ R$ {max:.2f}: {qtd}")
            print(f"O maior salário da faixa R$ {min:.2f} ~ {max:.2f} é: R$ {maior_salario:.2f}")
            print(f"Média de salários na faixa R$ {min:.2f} ~ R$ {max:.2f}: R$ {soma/qtd:.2f}")
            print(f"Pessoas com salários maiores do que o máximo de R$ {max:.2f}: {qtd_maior_que_max}")

