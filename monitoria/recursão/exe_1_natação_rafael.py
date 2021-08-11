"""
O Brasil brilhou em Tóquio nas Olimpíadas de 2021. 
Fomos ouro sobretudo nos esportes aquáticos, 
nos quais nadar é essencial. 
Vamos escrever um programa que receba a quantidade 
de metros a mergulhar e a profundidade e retorne, 
a cada metro, uma mensagem que atualiza a profundidade 
do mergulho. Detalhe: é proibido usar repetição!
"""
def natação(metros, profundidade = 0):
    if metros < 1:
        print("Chegou ao fundo/objetivo")
        # print(f"{profundidade}m de profundidade")
    else:
        print(f"{profundidade}m de profundidade")
        natação(metros-1, profundidade + 1)

print(natação(5))
