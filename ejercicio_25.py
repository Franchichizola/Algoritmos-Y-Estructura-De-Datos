def triangulo_pascal(n):
    triangulo = [[None]*n for _ in range(n)]
    
    def calcular(i, j):
        if j == 0 or j == i:
            triangulo[i][j] = 1
            return 1
        if triangulo[i][j] is not None:
            return triangulo[i][j]
        triangulo[i][j] = calcular(i-1, j-1) + calcular(i-1, j)
        return triangulo[i][j]
    
    for i in range(n):
        for j in range(i+1):
            calcular(i, j)
    
    for i in range(n):
        for j in range(i+1):
            print(triangulo[i][j], end=" ")
        print()

triangulo_pascal(5)
