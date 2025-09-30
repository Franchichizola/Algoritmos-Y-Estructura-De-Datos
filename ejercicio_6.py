def invertir(palabra):
    if len(palabra) <= 1:
        return palabra
    return palabra[-1] + invertir(palabra[:-1])

print(invertir("skibidi sigma"))