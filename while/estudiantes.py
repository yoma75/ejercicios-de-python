# Programa que permita determinar cuántos hombres y mujeres hay en un curso de 5 estudiantes.

estudiantes = []
hombre = mujer = x = 0 # Las tres variables tienen el mismo valor de cero
opc = ''

while x < 10:
    print('Eres hombre: ')
    print('Eres mujer: ')
    opc = input('Escoja la opcion: ')
    estudiantes.append(opc)
    print()
    x = x+1

for x in estudiantes:
    if x == 'hombre':
        hombre = hombre + 1    
    else:
        mujer = mujer + 1    

print(estudiantes)
print()

print(f'Total de mujeres: {mujer}')
print(f'Total de hombres: {hombre}')

