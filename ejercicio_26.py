def es_seguro(tablero, fila, columna, n):
    for i in range(fila):
        if tablero[i] == columna:
            return False
    for i in range(fila):
        if abs(tablero[i] - columna) == abs(i - fila):
            return False
    return True

def resolver_reinas(n):
    soluciones = []
    tablero = [-1] * n 

    def backtrack(fila):
        if fila == n:
            soluciones.append(tablero.copy())
            return
        for columna in range(n):
            if es_seguro(tablero, fila, columna, n):
                tablero[fila] = columna
                backtrack(fila + 1)
                tablero[fila] = -1  
    backtrack(0)
    return soluciones


soluciones = resolver_reinas(8)
print(f"Se encontraron {len(soluciones)} soluciones")
print(soluciones[0])
