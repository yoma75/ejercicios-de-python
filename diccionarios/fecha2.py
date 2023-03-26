# DESARROLLADO POR CHATGPT: Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

'''El programa comienza importando el módulo datetime para trabajar con fechas. Luego, pide al usuario la fecha en formato dd/mm/aaaa y la almacena en una cadena llamada fecha_str. Después, utiliza el método strptime() del objeto datetime para convertir la cadena a un objeto fecha. El segundo argumento de strptime() indica el formato de la cadena, en este caso %d/%m/%Y.

A continuación, crea una cadena con el formato deseado utilizando el método strftime() del objeto fecha. El formato %d de %B de %Y indica que queremos el día del mes (%d), seguido de la palabra "de", seguido del nombre completo del mes en minúsculas (%B), seguido de la palabra "de", y finalmente el año con cuatro dígitos (%Y).

Por último, muestra la fecha formateada por pantalla utilizando la función print().

Con esto, tendrás un programa que te permitirá convertir una fecha en formato dd/mm/aaaa a formato dd de mes de aaaa.'''


# Importamos el módulo datetime para trabajar con fechas
import datetime

# Pedimos al usuario la fecha en formato dd/mm/aaaa
fecha_str = input("Introduce una fecha en formato dd/mm/aaaa: ")

# Convertimos la cadena a un objeto fecha
fecha = datetime.datetime.strptime(fecha_str, '%d/%m/%Y')

# Creamos una cadena con el formato deseado
fecha_formateada = fecha.strftime('%d de %B de %Y')

# Mostramos la fecha formateada por pantalla
print(fecha_formateada)

