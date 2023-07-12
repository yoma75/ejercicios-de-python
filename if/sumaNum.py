#  Dados 3 numeros determinar si la suma de una pareja de ellos es igual al tercer numero, si se cumple esta condicion escribir: iguales o de lo contrario escribir: distintos

def numeros(a, b, c):
    if a + b == c or a + c == b or b + c == a:
        return 'Iguales'
    else:
        return 'Distintos'

print(numeros(3, 6, 9))  # Iguales
print(numeros(2, 3, 4))  # Distintos
