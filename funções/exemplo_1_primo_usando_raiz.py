import math
def primo(num):
    raiz = int(math.sqrt(num))
    i = 2
    while (i <= raiz) and ((num % i) != 0):
        i += 1
    
    if i > raiz:
        return True
    else:
        return False

# print(primo(7))
# print(primo(8))

for i in range(2, 1_000_000):
    if primo(i):
        print(i)