from ejercicio_10 import cantidad_digitos 

def invertir_numero(n):
    if n < 10:
        return n
    ultimo = n % 10
    return ultimo * (10 ** cantidad_digitos(n//10)) + invertir_numero(n // 10)

if __name__ == "__main__":
    print(invertir_numero(1111222345857))