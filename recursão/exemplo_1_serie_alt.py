# Exemplo: S = 1 + 3/2 + 5/3 + 7/4 + ... (n termos)
# Solução alternativa:

def serieR (n, nu = 1, de = 1.0) :
    res = nu / de
    if n > 1 :
        res = res + serieR (n - 1, nu + 2, de + 1)
    return res

print(serieR(1))
print(serieR(4))

# se quiser esconder os parâmetros:
def serie(n):
    return serieR(n, 1, 1.0)

print(serie(1))
print(serie(4))