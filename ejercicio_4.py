def potencia_r(b,e):
    if e == 0:
        return 1
    elif e > 0:
        return b * potencia_r(b, e - 1)
    else:
        return b / potencia_r(b, e + 1)

print(potencia_r(2,986))