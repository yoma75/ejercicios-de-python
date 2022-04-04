# Escribe una función llamada calificar_pelicula que reciba un parámetro rating (un número). Si el rating es menor a o igual a 5 la función debe retornar la cadena "Terrible!". Si el rating está entre 5 y 9 debe retornar la cadena "Interesante". Si el rating es 9 o más debe retornar la cadena "Increíble!".

# print(calificar_pelicula(5)) # "Terrible!"
# print(calificar_pelicula(8)) # "Interesante"
# print(calificar_pelicula(9)) # "Increíble!"


def calificar_pelicula(rating):
  if (rating <= 5):
    return 'Terrible!'
  elif ((rating > 5) and (rating < 9)):
    return 'Interesante'
  elif ((rating == 9 ) or (rating > 9)):
    return 'Increíble!'


print(calificar_pelicula(5)) # "Terrible!"
print(calificar_pelicula(8)) # "Interesante"
print(calificar_pelicula(9)) # "Increíble!"