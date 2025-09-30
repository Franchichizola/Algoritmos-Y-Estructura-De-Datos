def romano_a_decimal(NroRomano):
    valores_letras= {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,    
    }
    if len(NroRomano) == 0:
        return 0
    if len(NroRomano) > 1 and valores_letras[NroRomano[0]] < valores_letras[NroRomano[1]]:
        return (valores_letras[NroRomano[1]] - valores_letras[NroRomano[0]] + romano_a_decimal(NroRomano[2:] ))
    return valores_letras[NroRomano[0]] + romano_a_decimal(NroRomano[1:])

print(romano_a_decimal("MIX"))