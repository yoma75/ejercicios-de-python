# leer un caracter y deducir si esta situado antes o despues de la letra 'm' en orden alfabetico

caracter = input("Ingresa un carácter: ")

if caracter < 'm':
    print("El carácter está antes de la letra 'm' en el orden alfabético.")
elif caracter > 'm':
    print("El carácter está después de la letra 'm' en el orden alfabético.")
else:
    print("El carácter es la letra 'm'.")
