# * el asterisco: significa que los parametros son indefinidos

'''Parámetros de longitud variable *args:
- Los parámetros de LONGITUD VARIABLE se definen agregando un asterisco (*) antes del nombre del parámetro en la definición de la función.
- Los parámetros de longitud variable permiten que una función acepte un número arbitrario de argumentos posicionales.
- Los argumentos pasados a los parámetros de longitud variable se convierten en una tupla dentro de la función.'''

def lista(*valores):
  for x in valores:
    print(x, end=' ')  # 95 159 Hola 287

lista(95, 159, 'Hola', 287)
print('\n---------------------------------')

# ---------------------------------------------------------------------------------

'''
Parámetros de longitud variable **kwargs:
- Los parámetros de longitud variable de PALABRAS CLAVE se definen agregando dos asteriscos (**) antes del nombre del parámetro en la definición de la función.
- Los parámetros de longitud variable de palabras clave permiten que una función acepte un número arbitrario de argumentos de palabras clave.
- Los argumentos pasados a los parámetros de longitud variable de palabras clave se convierten en un diccionario dentro de la función.'''


def imprimir_datos(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

imprimir_datos(nombre="Juan", edad=25, ciudad="Bogotá")
