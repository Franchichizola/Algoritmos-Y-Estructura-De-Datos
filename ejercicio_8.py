def decimal_a_binario(Nro):
    if Nro == 0:
        return "0"
    if Nro == 1:
        return "1"
    return decimal_a_binario(Nro // 2) + str(Nro % 2)

print(decimal_a_binario(128))

