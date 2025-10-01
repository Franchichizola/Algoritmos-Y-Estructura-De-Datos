def auxiliar(lista, valor, indice = 0):
    if lista[indice] == valor:
        return indice
    else:
        return auxiliar(lista,valor,indice + 1)
    
def busqueda_sequencial(lista, valor):
    tamaño_original = len(lista)
    lista.append(valor)
    indice = auxiliar(lista,valor)
    lista.pop()
    if indice < tamaño_original:
        return True
    else:
        return False
    
print(busqueda_sequencial([0,1,2,3,4,5,6,7], 6))