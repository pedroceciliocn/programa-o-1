"""S3 = 150/20 – 156/30 + 162/50 – 170/80 + 174/120 - 184/170"""

def serie_S3(n, nu = 150, de = 10, nu_neg = -156, inc = 10, pos = True): 
    if pos == True:
        res = nu / de
    else:
        res = nu_neg/de
    if n > 1:
        if pos == True:
            return res + serie_S3(n - 1, nu + 12, de + inc, nu_neg, inc + 10, False)
        else:
            return res + serie_S3(n - 1, nu, de + inc, nu_neg - 14, inc + 10, True)
    return res

N = int(input("Dê o número de termos da sequência S: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_S3(N):.4f}")
    N = int(input("Dê o número de termos da sequência S: "))
    
############ alt  rafael ##################### correta
def serie_3(n, num_1 = 150, num_2 = 156, den = 10, inc = 10, sin = 1):
    if n <= 1:
        if sin > 0:
            res = sin * num_1 / den
        else:
            res = sin * num_2 / den
    else:
        if sin > 0:
            res = sin * num_1 / den + serie_3(n - 1, num_1, num_2 + 14, den + inc, inc + 10 , sin * -1)
        else:
            res = sin * num_2 / den + serie_3(n - 1, num_1 + 12, num_2, den + inc, inc + 10 , sin * -1)
    return res
    
N = int(input("Dê o número de termos da sequência S: "))
while N > 0:
    print(f"A soma dos {N} termos da sequência é: {serie_3(N):.4f}")
    N = int(input("Dê o número de termos da sequência S: "))