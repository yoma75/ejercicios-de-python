pares_list, impares_list = [], []

while (numero := int(input("Digite un número o 0 para detener: "))) != 0:
  (impares_list if numero % 2 else pares_list).append(numero)

print(f"\nSe digitó {len(impares_list)} números impares: {impares_list}")
print(f"Se digitó {len(pares_list)} números pares: {pares_list}")


# Uso del operador de walrus (:=): Permite asignar y evaluar una variable en la misma línea, simplificando el bucle while.
# Los contadores len(impares_list) y len(pares_list), cuentan los elementos directamente.
# Operador ternario para listas: Se usa (impares_list if numero % 2 else pares_list).append(numero) para añadir el número a la lista correspondiente en una sola línea.
