def busqueda(lista, valor, izquierda = 0, derecha = None):
    if derecha is None:
        derecha = len(lista) - 1

    if izquierda > derecha:
        return False

    medio = (izquierda + derecha) // 2

    if lista[medio] == valor:
        return True
    elif valor < lista[medio]:
        return busqueda(lista, valor, izquierda, medio - 1)
    else:
        return busqueda(lista, valor, medio + 1, derecha)


print(busqueda([1,2,3,4,5,6,7,8],2))