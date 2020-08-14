# Programa que determine si una persona es mayor de edad o no teniendo en cuenta el año actual y su año de nacimiento

def nacimiento(year):
    resultado = 2020 - year
    if resultado >= 18:
        return print(f'Usted nacio en el año {year} y es mayor de edad porque tiene: {resultado} años')
    else:
        return print(f'Usted nacio en el año {year} y es menor de edad porque tiene: {resultado} años')

print('')
nacimiento(1975)
nacimiento(2013)
nacimiento(1967)
nacimiento(2003)
nacimiento(1945)
