def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        print("No se puede dividir por cero")
        return 0
    else:
        return num1 / num2

while True:
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingrese su elección (1/2/3/4/5): ")

    if opcion == '5':
        break

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Ingrese números válidos")
        continue

    if opcion == '1':
        print("El resultado de la suma es: ", sumar(num1, num2))
    elif opcion == '2':
        print("El resultado de la resta es: ", restar(num1, num2))
    elif opcion == '3':
        print("El resultado de la multiplicación es: ", multiplicar(num1, num2))
    elif opcion == '4':
        print("El resultado de la división es: ", dividir(num1, num2))
