def aplicarAumento(precio):
    aumento = (precio / 100) * 5
    precio += aumento
    return precio

x = int(input("ingrese el precio: "))

precio_final = aplicarAumento(x)
print("el aumento del 5 es de", precio_final)