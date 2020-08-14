# Calcular la Suma de Tres Números e Incluir una Condición de Igualdad

def sumar_numeros(a, b, c):
    suma = a+b+c

    if a == b and a == c:
        suma *=3
    
    return suma

print(sumar_numeros(5,5,5))
print(sumar_numeros(3,4,2))




