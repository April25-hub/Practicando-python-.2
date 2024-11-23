def es_vocal(caracter):
    if caracter.lower() in "aeiouaeiou":
        return True
    return False

#esta linea dara un ejemplo de uso
print(es_vocal('a'))  #esta linea devuelve True
print(es_vocal('b'))  #esta linea devuelve False
