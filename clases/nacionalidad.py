class Nacionalidad:
  def __init__(self, nombre, pais):
    self.nombre = nombre
    self.pais = pais
  
  def presentacion(self, presento):
    return (f'Mi nombre es {presento.nombre} soy de {presento.pais}')


mexico = Nacionalidad('Laura', 'Mexico')
colombia = Nacionalidad('Jose', 'Colombia')

print(mexico.presentacion(mexico))  # Mi nombre es Laura soy de Mexico
print(f'{colombia.presentacion(colombia)}\n')  # Mi nombre es Jose soy de Colombia


'''Explicacion con ChatGPT: Este código define una clase llamada "Nacionalidad" que tiene dos atributos: "nombre" y "pais". Además, la clase tiene un método llamado "presentacion", que toma un objeto de tipo "Nacionalidad" como argumento y devuelve una cadena de texto que representa la presentación de esa persona.

El método "presentacion" utiliza la cadena de formato para crear una cadena que indica el nombre y el país de la persona que se está presente

Después de definir la clase "Nacionalidad", el código crea dos objetos de tipo "Nacionalidad" llamados "mexico" y "colombia", y les asigna valores para sus atributos "nombre" y "pais".

Finalmente, el código imprime el resultado de llamar al método "presentacion" en ambos objetos. En el primer caso, se llama al método con el objeto "mexico", lo que significa que la cadena resultante indica que Laura es de México. En el segundo caso, se llama al método con el objeto "colombia", lo que significa que la cadena resultante indica que José es de Colombia.

En resumen, este código define una clase que representa la nacionalidad de una persona y muestra cómo crear objetos de esa clase y llamar a sus métodos.'''