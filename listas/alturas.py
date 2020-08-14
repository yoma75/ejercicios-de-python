# Programa que permita calcular la estatura promedio de un grupo de 18 estudiantes y luego tomar las siguientes decisiones: 
# a) Si la estatura promedio es menor a 140 cm imprimir un mensaje que diga “Estudiantes muy bajos”. 
# b) Si la estatura promedio se encuentra entre 140 y 170 cm imprimir “Estudiantes de estatura normal”.
# c) Si la estatura promedio es mayor de 170 cm imprimir “Estudiantes muy altos”. 

altura_estudiante = list([])
i, suma_de_estaturas = 0, 0

while i < 5:
    estudiante = int(input('Digite su su estatura: '))
    altura_estudiante.append(estudiante)
    i = i+1

for x in altura_estudiante:
    suma_de_estaturas = suma_de_estaturas + x
    promedio = (suma_de_estaturas / len(altura_estudiante))

print()

if promedio <= 140:
    print('Estudiantes muy bajos')
elif promedio >= 141 and promedio <= 170:
    print('Estudiantes de estatura normal')
else:
    print('Estudiantes muy altos')



