# Exemplo: S = 1 + 3/2 + 5/3 + 7/4 + ... (n termos)
def serieR (n, nu = 1, de = 1.0) :
    if n <= 1:
        res = nu / de
    else:
        res = nu / de + serieR (n - 1, nu + 2, de + 1)
    return res

print(serieR(4))