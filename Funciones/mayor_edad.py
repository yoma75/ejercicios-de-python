# Programa que determine si una persona es mayor de edad o no teniendo en cuenta el año actual y su año de nacimiento

from datetime import datetime

def nacimiento(yearBorn):
  year_actual = datetime.now().year  # guarda solamente el año actual
  resultado = year_actual - yearBorn
    
  if resultado >= 18:
    return print(f'\nUsted nacio en el año {yearBorn} y es mayor de edad porque tiene: {resultado} años')
  else:
    return print(f'Usted nacio en el año {yearBorn} y es menor de edad porque tiene: {resultado} años')

nacimiento(1975)  # Usted nacio en el año 1975 y es mayor de edad porque tiene: 45 años
nacimiento(2013)  # Usted nacio en el año 2013 y es menor de edad porque tiene: 7 años
nacimiento(1967)  # Usted nacio en el año 1967 y es mayor de edad porque tiene: 53 años
nacimiento(2003)  # Usted nacio en el año 2003 y es menor de edad porque tiene: 17 años
nacimiento(1945)  # Usted nacio en el año 1945 y es mayor de edad porque tiene: 75 años

