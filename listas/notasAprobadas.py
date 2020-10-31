# Decir que materias debe de repetir el estudiante, notas sobre 10

asignaturas = ['Algebra', 'Quimica', 'Fisica', 'Calculo', 'Filosofia']
aprobadas = []

print('')

for x in asignaturas:    
    nota = float(input(f'Que nota has sacado en {x}: '))
    if nota >= 5:
        aprobadas.append(x)

# Elimina las que no cumplen con la condicion if
for z in aprobadas:
    asignaturas.remove(z)
print(f'\nTienes que repetir: {str(asignaturas)}'.upper())

