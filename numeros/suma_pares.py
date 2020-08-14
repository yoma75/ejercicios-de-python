# Sumar los numeros pares de 1 a 100

suma = 0
print('')

for i in range(2, 100, 2):    
    print(i)
    suma += i

print(f'El total de la suma de los numeros pares es: {suma}') 
