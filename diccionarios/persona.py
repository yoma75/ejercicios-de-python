# Escribir un programa que pregunte al usuario su nombre, edad, ciudad y lo guarde en un diccionario. Despúes debe mostrar por pantalla el mensaje 
# <nombre> tiene <edad> años, vive en <ciudad> 

name = input('Tu nombre: ')
age = int(input('Edad: '))
city = input('Ciudad donde vives: ')
person = {'nombre': name, 'edad': age, 'ciudad': city}

print(person['nombre'], 'tiene', person['edad'], 'años, y vive en', person['ciudad'])
print(person)
