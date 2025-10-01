def calcular_f(n):
    if n == 1:
        return 2
    if n >= 2:
        return n + 1/calcular_f(n-1)
    

print(calcular_f(2))