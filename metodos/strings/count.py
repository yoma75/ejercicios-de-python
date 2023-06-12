# count: devuelve una cuenta de las veces que aparece una subcadena en la cadena:

frase = ("La casa es grande y es comoda")
print(frase.count('a'))  # 5


# Cuenta cuantas veces se encuentra 'es' desde el indice 2 hasta el indice 45
print(f'La palabra "es" se encuentra {frase.count("es", 2, 45)} veces')  # 2 veces
