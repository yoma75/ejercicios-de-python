# Crea un programa con un bucle for y una declaración continue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada:


print('0 1 6 5 0 3 1 8 0 6 5 1 0')

for digit in "0165031806510":
    if digit == "0":
        print("x", end=" ")
        continue
    print(digit, end=" ")
