# Escribir un programa que pregunte al usuario su nombre, edad, ciudad y lo guarde en un diccionario. Despúes debe mostrar por pantalla el mensaje 
# <nombre> tiene <edad> años, vive en <ciudad> 

name = input('Tu nombre: ')
age = int(input('Edad: '))
city = input('Ciudad donde vives: ')
person = {'nombre': name, 'edad': age, 'ciudad': city}

print(person['nombre'], 'tiene', person['edad'], 'años, y vive en', person['ciudad'])
print(person)

# Tu nombre: melba
# Edad: 87
# Ciudad donde vives: Bogotá
# melba tiene 87 años, y vive en bogota
# {'nombre': 'melba', 'edad': 87, 'ciudad': 'bogota'}
