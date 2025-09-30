def producto_r(x,y):
    if x == 0 or y == 0:
        return 0
    elif y > 0:
        return x + producto_r(x, y - 1)
    else:
        return -producto_r(x, -y)
        
print(producto_r(4,-6))