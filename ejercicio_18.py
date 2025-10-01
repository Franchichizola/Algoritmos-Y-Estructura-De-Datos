def mostrar_matriz(matriz, indice = [0,0]):
    if indice[0] >= len(matriz):
        return
    print(matriz[indice[0]][indice[1]], end="")
    if len(matriz[indice[0]]) - 1 == indice[1]:
        print()
        indice[0] += 1 
        indice[1] = 0
        mostrar_matriz(matriz,indice)
    else:
        indice[1] += 1 
        mostrar_matriz(matriz,indice)
    
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mostrar_matriz(matriz)