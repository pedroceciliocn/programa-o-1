"""
2) Modifique a função recursiva de Fibonacci para retornar o total de chamadas de função. Por
exemplo: para encontrar o quinto termo da sequência (considerando que 0 é o primeiro), foram
necessárias 8 chamadas recursivas.
"""


# def fibonacci_r(n, t0 = 1, t1 = 0):
#     if n <= 1:
#         res = t1
#     else:
#         res = fibonacci_r(n - 1, t1, t0 + t1)
#     return res

# print(fibonacci_r(5))

# count = 0
# def fibonacci_r(n, t0 = 1, t1 = 0):
#     global count
#     if n <= 1:
#         res = t1
#     else:
#         count += 1
#         res = fibonacci_r(n - 1, t1, t0 + t1)
#     return res

# print(fibonacci_r(5), count)


# count = 0
# def fibR(n, t1 = 1, res = 0):
#     global count    
#     if n > 1:
#         count +=1
#         res = fibR(n - 1, res, t1 + res)
#     return res

# print(fibR(5), count)

count = 0
def fibonacci(n):
    global count
    count +=1
    if n <= 1:
        return n
    else:
        
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5), count)