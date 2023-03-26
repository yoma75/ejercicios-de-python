# Pedir la usuario 3 frases y guardarlas en un fichero como  "frases.txt"
# Añadir una cuarta frase al fichero anterior
# Mostrar el contenido de "frases.txt", procediendo de línea con un número correlativo


for x in range(3):
  frases = input('Escriba una frase: ')
  fichero = open('frases.txt', 'a')
  fichero.writelines(f'{frases}\n')


cuartaFrase = ['Esta es la cuarta frase\n']
fichero.writelines(cuartaFrase)
fichero.close()


fichero = open('frases.txt')
print(fichero.read())
fichero.close()