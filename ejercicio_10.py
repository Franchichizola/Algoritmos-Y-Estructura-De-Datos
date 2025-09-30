def cantidad_digitos(n):
    if n <= 0:
        return 0
    return 1 + cantidad_digitos(n//10)

print(cantidad_digitos(1234567890))