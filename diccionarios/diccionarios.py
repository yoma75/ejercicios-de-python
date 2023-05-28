# Los diccionarios pueden almacenar cualquier tipo de valor, incluidos otros diccionarios. Esto le permite modelar datos complejos según sea necesario.

gato = {
    'name': 'Michin',
    'edad': 1
}


# lectura de valores se puede hacer de dos formas:
print(gato.get('name'))
print(gato['name'])


# UPDATE: permite modificar varios valores en una sola operacion
gato.update({
    'name': 'Felix',
    'edad': 9
})

# Tambien se puede asi:
# gato['name'] = 'Felix'
# gato['edad'] = 9


# Agrega otro diccionario en el anterior
gato['otros'] = {
    'hobbie': 'jugar',
    'comida-favorita': 'salmon'
}

print(gato)
# {'name': 'Felix', 'edad': 9, 'otros': {'hobbie': 'jugar', 'comida-favorita': 'salmon'}}


print(f'{gato["name"]}, le gusta: {gato["otros"]["comida-favorita"]}')
# Felix, le gusta: salmon
