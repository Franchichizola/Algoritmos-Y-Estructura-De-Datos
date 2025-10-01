def auxiliar(numero, prueba):
    if prueba * prueba > numero:
        return prueba - 1
    return auxiliar(numero,prueba + 1)
    

def raiz_cuadrada(n):
    if n < 0:
        return "error"
    else:
        return auxiliar(n,0)
    
print(raiz_cuadrada(100))