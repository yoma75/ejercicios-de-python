# . Programa que permita determinar si un estudiante que recibe 5 notas gana o no la materia de Programación de Software. Se gana la materia si el promedio es mayor o igual a 4.0

notas_alumno = []
x, suma = 0, 0

while x < 5:
    calificacion = int(input(f'Digite la nota # {x+1}: ... '))
    notas_alumno.append(calificacion)
    x = x+1

print()

for i in notas_alumno:
    suma = suma + i
    promedio = round(suma / len(notas_alumno))

if promedio >= 40:
    print(f'Su calificacion es: {promedio} APROBADO')
else:
    print(f'Su calificacion es: {promedio} NO APROBADO')
