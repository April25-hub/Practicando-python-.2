def sum_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def multip(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

#esta linea dara un ejemplo de uso
print(sum_lista([1, 2, 3, 4]))  #devuelve 10
print(multip([1, 2, 3, 4]))  #devuelve 24
