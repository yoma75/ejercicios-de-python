# Uso Básico del Operador de Asignación Walrus de Python 3.8.0

# := introducir la asignación en expresiones

cadena = 'Python'

if (x := len(cadena)) > 5:    
    print(f'\nLa cadena de caracteres "{cadena}" tiene mas de 5 caracteres; exactamente: {x}'.upper())
