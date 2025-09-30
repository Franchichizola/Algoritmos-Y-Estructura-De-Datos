def suma_enteros_r(n):
    if n == 1:
        return 1 
    else:
        return n + suma_enteros_r(n - 1)
    
print(suma_enteros_r(6))