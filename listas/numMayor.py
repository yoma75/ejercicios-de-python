# pedir tres numeros por teclado y decir cual es el mayor

numeros = [float(input("Ingrese el primer número: ")), 
           float(input("Ingrese el segundo número: ")), 
           float(input("Ingrese el tercer número: "))]

mayor = max(numeros)

print("El número mayor es:", mayor)
