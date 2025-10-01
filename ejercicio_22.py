def usar_la_fuerza(mochila,objetos_sacados=0):
    if not mochila:
        return (False, objetos_sacados)
    objeto_actual = mochila[0]
    objetos_sacados_actual = objetos_sacados + 1
    if objeto_actual == "sable de luz":
        return (True, objetos_sacados_actual)
    else:
        return usar_la_fuerza(mochila[1:], objetos_sacados_actual)

print(usar_la_fuerza(["comida", "mapa estelar", "botiquín", "sable de luz", "ganzúa"]))

