# Calcular el area de un triangulo

# area = base * altura / 2

# Para que el usuario no escriba cadenas de caracteres
base = None
altura = None 

while True:
    try:
        print()
        base = float(input('Escriba la base del triangulo: '.upper()))
        break;
    except:
        print('Debe escribir un numero')

while True:
    try:
        altura = float(input('Escriba la altura del triangulo: '.upper()))
        break;
    except:
        print('Debe escribir un numero')

print()
area = base * altura / 2

print(f'El area del triangulo es de: {area}')

