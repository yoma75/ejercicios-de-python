# break: termina el ciclo inmediatamente y sale del programa

for x in range(10):
  if x % 2 == 0:
    print('Par')  # si es PAR
    break
  print(x)  

print('Hola mundo\n')  


# ---------------------------------------------------------------------------

# continue: termina la iteración que se esta ejecutando y continua con la siguiente

for x in range(10):
  if x % 2 == 0:
    print('aqui va un numero par')  # si es PAR
    continue
  print(x)  # muestra el número si es IMPAR

print('Hola mundo')  


# par
# 1
# par
# 3
# par
# 5
# par
# 7
# par
# 9
# Hola mundo   