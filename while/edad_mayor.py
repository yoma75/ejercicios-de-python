# Programa que permita determinar cual es la edad mayor y menor en un grupo de 5 estudiantes. 

lista = []
i = 0

while i < 5:
    edad = int(input('Cual es tu edad: '))
    lista.append(edad)
    i = i + 1

print()
print('La edad mayor es: {} años'.format(max(lista)))
print('La edad menor es: {} años'.format(min(lista)))
