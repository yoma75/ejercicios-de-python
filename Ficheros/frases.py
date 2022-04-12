# Pedir la usuario 3 frases y guardarlas en un fichero como  "frases.txt"
# Añadir una cuarta frase al fichero anterior
# Mostrar el contendio de "frases.txt", procediendo da línea con un número correlativo


for x in range(4):
  frases = input('Escriba una frase: ')

fichero = open('frases.txt', 'a')
fichero.writelines(frases)

cuartaFrase = ['Esta es la cuarta frase\n']
fichero.writelines(cuartaFrase)

# leerContenido = fichero.readlines()
# print(leerContenido)

fichero.close()

