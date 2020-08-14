# Programa para calcular la edad promedio de un grupo de 15 estudiantes

estudiantes = []
i=sumar = 0

while i < 5:
    edad = int(input('Cual es tu edad: '))
    estudiantes.append(edad)
    i = i+1

for x in estudiantes:
    sumar = sumar + x
    promedio = round(sumar / len(estudiantes))

print()
print('La edad promedio del grupo es de: {} años '.format(promedio))




