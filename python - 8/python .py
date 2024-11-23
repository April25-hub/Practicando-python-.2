def superposicion(lista1, lista2):
    for item1 in lista1:
        for item2 in lista2:
            if item1 == item2:
                return True
    return False

#esta linea dara un ejemplo de uso
print(superposicion([1, 2, 3], [4, 5, 6]))  #devuelve False
print(superposicion([1, 2, 3], [3, 4, 5]))  #devuelve True
