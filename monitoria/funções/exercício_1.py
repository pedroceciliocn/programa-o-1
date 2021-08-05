"""1) Faça um programa que verifique se o nome de pessoas possuem mais de 6 caracteres. 
Esta checagem deve ser feita através de uma função que irá retornar True caso o nome 
tenha 7 caracteres ou mais, e False caso o nome tenha até 6 caracteres."""

def verifica(nome):
    if len(nome) > 7:
        return True
    else:
        return False


