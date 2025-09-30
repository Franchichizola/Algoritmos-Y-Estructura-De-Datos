def logaritmo(n,b):
    if n < b:
        return 0
    return 1 + logaritmo(n // b, b)

print(logaritmo(128,2))