def reversa(vector,indice=None):
    if indice == None:
        indice = len(vector) - 1
    if indice < 0:
        return
    print(vector[indice])
    return reversa(vector,indice-1)

reversa([1,2,3,4,5,6,5,4,3,6,7])