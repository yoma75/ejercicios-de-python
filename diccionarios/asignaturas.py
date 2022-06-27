'''Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.'''


#           llave     : valor 
curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

total_creditos = 0

for asignatura, creditos in curso.items():
    print(f'{asignatura} tiene: {creditos} creditos')
    total_creditos += creditos

print(f'\nTotal de creditos del curso: {total_creditos}')

# Matematicas tiene: 6 creditos
# Fisica tiene: 4 creditos
# Química tiene: 5 creditos

# Total de creditos del curso: 15

