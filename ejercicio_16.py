def sucesion(an):
    if an == 1:
        return 2
    return -3 * sucesion(an-1)

def imprimir(an, actual=1):
    if actual > an:
        return
    print(sucesion(actual))
    imprimir(an, actual + 1)


imprimir(5)