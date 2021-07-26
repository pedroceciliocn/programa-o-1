"""
Faça um programa que recebe do usuário duas strings. Em seguida, escreva uma função que recebe
essas duas strings como parâmetro e retorna True/False informando se elas são um anagrama. 
Letras maiúsculas e minúsculas devem ser tratadas da mesma maneira. Ao final do programa, 
imprima a seguinte mensagem:
- A palavra "string1" é um anagrama de "string2" (se for um anagrama)
- A palavra "string1" não é um anagrama de "string2" (se não for um anagrama)
"""

def é_anagrama(string1, string2):
    lista_chars = list(string1.lower())
    string2 = string2.lower()
    contador = 0
    for letra in lista_chars:
        if letra in string2:
            contador += 1
    if contador == len(string2):
        return print(f"A palavra '{string1}' é um anagrama de '{string2}'.")
    else:
        return print(f"A palavra '{string1}' não é um anagrama de '{string2}'.")


é_anagrama('aipim', 'pimai')
é_anagrama('amordoteste', 'roma')
é_anagrama('abcde', 'EdcaB')
é_anagrama('abcdee', 'EdcaB')



