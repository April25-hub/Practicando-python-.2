def longitud(objeto):
    contador = 0
    for i in objeto:
        contador += 1
    return contador

#esta linea dara un ejemplo de uso
print(longitud([1, 2, 3, 4]))  #esta linea devuelve 4
print(longitud("hola"))  #esta linea devuelve 4
