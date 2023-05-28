planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

lunas = planet_moons.values()
total_planetas = len(planet_moons.keys())

total_lunas = 0
for x in lunas:
    total_lunas = total_lunas + x

promedio = total_lunas / total_planetas


print(f'Cada planeta tiene un promedio de {promedio} lunas')
# Cada planeta tiene un promedio de 17.833333333333332 lunas

