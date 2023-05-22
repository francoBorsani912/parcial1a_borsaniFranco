def reemplazarCaracteres(cadena,primer_caracter,segundo_caracter):
    contador = 0
    cadena = str
    for letra in cadena:
        if letra == primer_caracter:
            cadena.replace(primer_caracter,segundo_caracter)
            contador += 1
    print(contador)
    return cadena

x = "la vida es muy bella"

x = reemplazarCaracteres(x,"a","u")
print(x)