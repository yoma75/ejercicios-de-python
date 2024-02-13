# Las variables que se crean fuera de una función se conocen como variables globales, pueden ser utilizadas dentro y fuera de una funcion

x = 'increible'

def myfunc():
  print(f'Python es {x}' )

myfunc()  # Python es increible

# --------------------------------------------------------------------------------------------------------------

# Si crea una variable con el mismo nombre dentro de una función, esta variable será local y solo se puede usar dentro de la función. 
# La variable global con el mismo nombre se mantendrá como estaba, global y con el valor original.

a = "increible"

def myfunc():
  a = "fantastico"
  print("Python is " + a)  # Python is fantastico

myfunc()

print("Python is " + a)  # Python is increible
