

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

numero = 0

while numero != secret_number:
  numero = int(input("\nDigite un numero de tres cifras: "))

  if numero == secret_number:
    print("¡Bien hecho, muggle! Eres libre ahora.")  
  else:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")


# OPERADOR TERNARIO
# print("¡Bien hecho, muggle! Eres libre ahora." if numero == secret_number else "¡Ja, ja! ¡Estás atrapado en mi bucle!")
