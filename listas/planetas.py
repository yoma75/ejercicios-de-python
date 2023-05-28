planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Uranio", "Neptuno"]

user_planet = input('\nIngrese el nombre de un planeta (primera letra en mayuscula): ')


# Acceder al index del planeta ingresado por el usuario
index_planeta = planetas.index(user_planet)


print(f'Planetas mas cercanos a la tierra: {planetas[0:index_planeta]}\n')
print(f'Planetas mas lejanos a la tierra: {planetas[index_planeta + 1:]}\n')

