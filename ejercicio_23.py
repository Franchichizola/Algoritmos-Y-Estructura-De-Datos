def resolver_laberinto(laberinto):
    n = len(laberinto)
    camino = [[0]*n for _ in range(n)]  
    
    def es_valido(x, y):
        return 0 <= x < n and 0 <= y < n and laberinto[x][y] == 0 and camino[x][y] == 0
    
    def buscar(x, y):
        if x == n-1 and y == n-1:
            camino[x][y] = 1
            return True
        
        if es_valido(x, y):
            camino[x][y] = 1  
            
            if buscar(x+1, y):  
                return True
            if buscar(x, y+1):  
                return True
            if buscar(x-1, y):  
                return True
            if buscar(x, y-1):  
                return True
            
            camino[x][y] = 0
            return False
        
        return False
    
    if buscar(0, 0):
        return camino
    else:
        return None  

laberinto = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]

camino = resolver_laberinto(laberinto)

if camino:
    for fila in camino:
        print(fila)
else:
    print("No hay salida posible")
