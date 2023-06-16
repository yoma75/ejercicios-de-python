# super: se utiliza para dar acceso a métodos y propiedades de una clase primaria o hermana.
# La función devuelve un objeto que representa la clase principal

class Padre:
  def __init__(self, txt):
    self.mensaje = txt

  def mostrarMensaje(self):
    print(self.mensaje)  # Hello, and welcome!

class claseHija(Padre):
  def __init__(self, txt):
    super().__init__(txt)

# Instancia
x = claseHija("Hello, and welcome!")

x.mostrarMensaje()


'''
Este código define dos clases: "Padre" y "claseHija". 
La clase "claseHija" es una subclase de la clase "Padre", lo que significa que hereda todas las propiedades y métodos de la clase "Padre".

La clase "Padre" tiene un constructor `__init__` que toma un argumento `txt` y asigna ese valor a la variable de instancia `self.mensaje`. También tiene un método llamado `mostrarMensaje`, que simplemente imprime el valor de `self.mensaje`.

La clase "claseHija" también tiene un constructor `__init__`, pero en este caso, utiliza la función `super()` para llamar al constructor de la clase "Padre" y pasarle el argumento `txt`. Esto asegura que la inicialización de la clase "Padre" se realice correctamente.

Luego, se crea una instancia de la clase "claseHija" llamada "x" pasando el argumento "Hello, and welcome!" al constructor. Esto significa que se llama al constructor de la clase "Padre" y se asigna el valor "Hello, and welcome!" a la variable `self.mensaje` en la instancia "x".

Finalmente, se llama al método `mostrarMensaje` en la instancia "x", lo que imprime el valor de `self.mensaje`. En este caso, el mensaje impreso será "Hello, and welcome!".

En resumen, este código muestra un ejemplo de herencia de clases, donde una subclase hereda propiedades y métodos de una superclase.
'''

# PORQUE la clase mostrarMensaje se dice que es un metodo y no una funcion?

# En el contexto de la programación orientada a objetos, una función definida dentro de una clase se llama método. Un método es una función que está asociada con un objeto y puede acceder a los datos del objeto (variables de instancia) y manipularlos.

# la diferencia principal entre un método y una función en el contexto de la programación orientada a objetos es que un método está asociado con una clase u objeto y puede acceder y manipular los datos del objeto, mientras que una función es un bloque de código independiente que se puede invocar en cualquier lugar del programa sin estar necesariamente relacionado con un objeto o una clase.
