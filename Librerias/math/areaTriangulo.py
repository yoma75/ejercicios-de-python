# Calcular el area de un triangulo

# area = base * altura / 2

# Para que el usuario no escriba cadenas de caracteres
base = None
altura = None 

while True:
    try:
        print()
        base = float(input('Escriba la base del triángulo: '.upper()))
        break;
    except:
        print('Debe escribir un numero')

while True:
    try:
        altura = float(input('Escriba la altura del triángulo: '.upper()))
        break;
    except:
        print('Debe escribir un número')

print()
area = base * altura / 2

print(f'El área del triángulo es de: {area}')
