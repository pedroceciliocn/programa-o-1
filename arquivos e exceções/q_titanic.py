fim = False
sum_ages = 0
total_survived = 0
man_survived = 0
woman_survived = 0

while not fim:
    try:
        nome_arquivo = 'titanic (cópia).txt'
        titanic_original = open(nome_arquivo, 'r')
        titanic_novo = open('titanic.novo.txt', 'w')
        with titanic_original, titanic_novo:
            for passageiro in titanic_original:
                PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked = passageiro.split(sep = ',')
                if (Survived) == '1':
                    sum_ages += float(Age)
                    total_survived += 1
                    if (Sex) == 'male':
                        man_survived += 1
                        titanic_novo.write(f'{Name} {Sex} {Age}\n')
                    else:
                        woman_survived += 1
                        titanic_novo.write(f'{Name} {Sex} {Age}\n')
    except FileNotFoundError:
        print("Arquivo informado pelo usuário não encontrado. Digite um nome válido.")
    else:
        print(f"Tarefa realizada com sucesso.")
        print(f"Homens sobreviventes: {man_survived}")
        print(f"Mulheres sobreviventes: {woman_survived}")
        print(f"Média de idades dos sobreviventes: {sum_ages/total_survived:.2f} anos")
        fim = True