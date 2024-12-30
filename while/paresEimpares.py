# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares y los muestre.
# El programa termina cuando se ingresa un cero.

num_impares, num_pares = 0  # Las dos variables con 0
pares_list, impares_list = [], []

numero = int(input("Digite un numero o digite 0 para detener: "))

while numero != 0:
  if numero % 2 == 1:  # Verificar si el número es impar
    impares_list.append(numero)
    num_impares += 1  # Incrementar el contador de números impares
  else:
    pares_list.append(numero)
    num_pares += 1  # Incrementar el contador de números pares
  
  numero = int(input("Digite un numero o digite 0 para detener: "))

print(f"\nSe digito {num_impares} numeros impares los cuales son: {impares_list}")
print(f"Se digito {num_pares} numeros pares los cuales son: {pares_list}")
