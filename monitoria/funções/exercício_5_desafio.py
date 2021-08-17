"""5) DESAFIO: Desafio: Faça um programa que crie multiplicadores. 
Seu programa deve conter uma função chamada createMultiplier. 
Esta função deve receber um número e retornar uma função que é a multiplicadora desse número. 
Verifique o funcionamento:

duplicate = createMultiplier(2)
triplicate = createMultiplier(3)

print(f"the double of 2 is {duplicate(2)}")
print(f"the triple of 2 is {triplicate(3)}")
"""

def createMultiplier(number):
    return lambda multiplier: number * multiplier

quadruplicate = createMultiplier(4)

print(f"the quadruple of 2 is {quadruplicate(2)}")



#### SEM USAR LAMBDA

def multiplier(multiple):
    def calculate(number):
        return number * multiple
    return calculate

multiply_by_4 = multiplier(4)

print(multiply_by_4(2))