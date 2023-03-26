# Crea un programa con un bucle for y una declaración continue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada:


print('0 1 6 5 0 3 1 8 0 6 5 1 0')

for digit in "0165031806510":
    if digit == "0":
        print("x", end=" ")  # 0 1 6 5 0 3 1 8 0 6 5 1 0
        continue
    print(digit, end=" ")    # x 1 6 5 x 3 1 8 x 6 5 1 x


'''El programa utiliza un bucle for para iterar sobre cada uno de los dígitos de la cadena cadena. Dentro del bucle, se verifica si el dígito es igual a '0'. Si es así, el programa reemplaza el dígito con la letra 'x' y utiliza la declaración continue para pasar a la siguiente iteración sin ejecutar el código restante en el bloque de código del bucle. Si el dígito no es igual a '0', se imprime el dígito original en la consola junto con un espacio en blanco. El argumento end=' ' en la función print() se utiliza para asegurarse de que los dígitos y la letra 'x' estén separados por un espacio en blanco.'''