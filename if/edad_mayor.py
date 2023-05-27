# Programa que permita determinar cuántos estudiantes son mayores y menores de edad en un grupo de 10 estudiantes. 

estudiantes = []
i = 0
mayor = 0
menor = 0

while i < 10:
    edad = int(input('Cual es su edad: '))
    estudiantes.append(edad)
    i = i+1

    if edad >= 18:
        mayor = mayor+1
    else:
        menor = menor+1

print()
print(f'Existen {mayor} estudiantes mayores de edad')
print(f'Existen {menor} estudiantes menores de edad')
