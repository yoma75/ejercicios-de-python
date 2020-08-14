# Uso Básico del Operador de Asignación Walrus de Python 3.8.0

# := introducir la asignacion en expresiones

cadena = 'Python'

if (x := len(cadena)) > 5:
    print()
    print(f'La cadena de caracteres {cadena} tiene mas de 5 caracteres; exactamente: {x}'.upper())
    

