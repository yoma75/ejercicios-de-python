def palindromo(palabra):    
    # Reemplazar todos los espacios por un string vacío
    palabra = palabra.replace(' ', '')
    palabra = palabra.upper()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
        

# indica que desde aquí ejecuta el codigo
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')    


# punto de entrada (Entry Point) de un programa en python
if __name__ == "__main__":
    run()
    