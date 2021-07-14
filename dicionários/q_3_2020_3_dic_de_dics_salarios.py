"""
Questão 3 – Faça um programa Python para ler uma tabela de alunos onde:
    • Cada aluno tem uma matrícula (int), um nome (string) e uma idade (int).
    • A leitura da tabela pára com uma matrícula que não seja positiva.
    • O usuário só pode digitar no máximo 200 alunos.
Depois o usuário informará um inteiro positivo N, seguido por uma série de N intervalos
de idades (idades mínima e máxima), e o programa deve imprimir, para cada intervalo
digitado pelo usuário, os dados dos alunos que se enquadram no intervalo, seguidos pelo
número de alunos do intervalo. Caso a idade mínima de algum intervalo seja maior do
que a idade máxima, o programa deve simplesmente imprimir uma mensagem de erro e
continuar
"""
should_continue = True
quantidade_alunos = 0
alunos = {}

while should_continue and quantidade_alunos < 200:
  matricula = int(input("Digite a matrícula: "))
  if matricula < 0:
    should_continue = False
  else:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    alunos[matricula] = {'nome': nome, 'idade': idade}
    quantidade_alunos += 1
print(f"Leitura concluída \n{alunos}") # dicionario de dicionarios

intervalos = int(input("Digite o número de intervalos: "))
for current in range(intervalos):
  count = 0
  limite_inferior = int(input('Digite o limite inferior: '))
  limite_superior = int(input('Digite o limite superior: '))
  if limite_superior < limite_inferior:
    print("O limite superior deve ser maior que o inferior!")
  else:
    for matricula in alunos.keys():
      aluno = alunos[matricula]
      if aluno['idade'] >= limite_inferior and aluno['idade'] <= limite_superior:
        count += 1
        print('nome: {}, idade: {}'.format(aluno['nome'], aluno['idade']))
    print(f'existem {count} alunos no intervalo  {limite_inferior} ~ {limite_superior}')