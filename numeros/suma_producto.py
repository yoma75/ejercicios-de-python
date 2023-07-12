# calcular  la suma y el producto de los numeros pares comprendidos entre 20 y 30 ambos inclusive

sumaNumeros = []
suma = 0
producto = 1

for numero in range(20, 32):
    if numero % 2 == 0:
        sumaNumeros.append(numero)
        suma += numero
        producto *= numero

print(sumaNumeros)  # [20, 22, 24, 26, 28, 30]

print(f"La suma de los números pares es: {suma}")  # La suma de los números pares es: 150
print(f"El producto de los números pares es: {producto:,.0f}")  # 230,630,400

# El producto es el resultado de multiplicar varios números entre sí. 
# En este ejemplo, el rango es de 20 a 30, los números pares serían 20, 22, 24, 26, 28 y 30. 
# Entonces, el producto de estos números sería 20 * 22 * 24 * 26 * 28 * 30.
