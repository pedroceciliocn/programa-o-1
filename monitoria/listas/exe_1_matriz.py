"""
Desenvolva um algoritmo
que crie duas matrizes 2x2
usando listas dentro de
listas. Tenha como entrada
o valor de cada ponto
dessas duas matrizes,
como saída, uma terceira
matriz que tenha os
maiores valores de cada
ponto entre as duas
matrizes criadas.
"""
m_1 = []
m_2 = []
m_3 = []
for i in range(2):
    m_1.append([0]*2)
    m_2.append([0]*2)
    m_3.append([0]*2)

for i in range(2):
    for j in range(2):
        m_1[i][j] = int(input(f"Dê o elemento {i+1} {j+1} da matriz 1: "))
        m_2[i][j] = int(input(f"Dê o elemento {i+1} {j+1} da matriz 2: "))
        if m_1[i][j] >= m_2[i][j]:
            m_3[i][j] = m_1[i][j]
        else:
            m_3[i][j] = m_2[i][j]

for i in range(2):
    print(m_3[i])
