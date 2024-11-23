def es_palindromo(palabra):
    return palabra == palabra[::-1]

#esta lina dara un ejemplo de uso
print(es_palindromo("radar"))  # Devuelve True
print(es_palindromo("python"))  # Devuelve False
