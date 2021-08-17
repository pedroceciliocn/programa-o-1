"""
1 – A média ponderada de N números é a soma dos produtos de cada um deles multiplicados por
seus respectivos pesos; o resultado da multiplicação é então dividido pela soma dos pesos. A
média ponderada é utilizada em diversas disciplinas para calcular os resultados dos alunos
considerando duas avaliações parciais com pesos variáveis. As regras para definição do resultado
são as seguintes:
    Se a média do aluno for maior ou igual a sete, o aluno “está
    aprovado”.
    
    Se a média do aluno for menor que três, o aluno “está reprovado”.
    
    Se a média do aluno for menor que sete e maior ou igual a três, ele
    “fará prova final”.

Faça uma subrotina Python do tipo procedimento que leia as notas das duas avaliações parciais
de um único aluno, calcule sua média, e imprima seu resultado na seguinte frase: "O aluno
obteve média ____ e ___________." Os pesos a serem utilizados no procedimento são
opcionalmente passados como parâmetros e, se não forem informados, seus valores devem ser 1.
O seu programa inicialmente deve ler o nome da disciplina, os pesos a serem usados nos
cálculos das médias e depois o número de alunos N. Em seguida, deve usar o procedimento
acima para processar as notas dos N alunos.
"""

def aprovação(disciplina, nota_1, nota_2, peso_nota_1 = 1, peso_nota_2 = 1):
    ponderada = ((nota_1 * peso_nota_1) + (nota_2 * peso_nota_2)) / (peso_nota_1 + peso_nota_2)
    if ponderada >= 7:
        print(f"O aluno obteve média {ponderada:.2f} na {disciplina} e está aprovado")
    elif ponderada >= 3:
        print(f"O aluno teve média {ponderada:.2f} na {disciplina} e fará a prova final")
    else:
        print(f"O aluno teve média {ponderada:.2f} na {disciplina} e está reprovado")


fim = False
while not fim:
    try:
        nome_disciplina = input("Dê o nome da disciplina: ")
        peso_1 = float(input("Dê o peso da primeira nota: "))
        peso_2 = float(input("Dê o peso da segunda nota: "))
        N = int(input("Dê o numero N de alunos: "))
        while N < 0:
            N = int(input("Dê o numero N de alunos (positivo!): "))
    except ValueError:
        peso_1, peso_2 = 1.0
        print("Valor errado!")
    else:
        fim = True


fim = False
i = 1
while not fim:
    while i <= N:
        try:
            n_1 = float(input(f"Digite a nota 1 do aluno {i}: "))
            n_2 = float(input(f"Digite a nota 2 do aluno {i}: "))
            aprovação(nome_disciplina, n_1, n_2, peso_1, peso_2)
        except ValueError:
            print(f"Você passou algo diferente de um número para as notas!")         
        else:
            i += 1
            fim = True
