# se define una funcion que realice la verificacion de si la palabra se escribe igual al derecho y al revez 
def palindromo(palabra):
    palabra = palabra.replace(' ', '') # el metodo repleace, remplaza una palabra por la otra 
    palabra = palabra.lower() # el metodo lower pone los caracteres en letra minuscula
    palabra_invertida = palabra[::-1] # a travez de los slices podemos imprimir cierta parte del texto
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():# esto es una buena practica para inicializar funciones
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':# de esta forma invocamos la funcion principal del codigo
    run()