class Encapsulamiento:
  __privado_atributo = 'Soy un ATRIBUTO que nos vas a poder acceder desde afuera de la clase'

  def __privado_metodo(self):
    print('Soy un METODO que nos vas a poder acceder desde afuera de la clase')
  

  # para que salga sin error:
  def publico_atributo(self):
    return self.__privado_atributo  
  
  def publico_metodo(self):
    return self.__privado_metodo()


e = Encapsulamiento()

e.publico_atributo
print(e)  # <__main__.Encapsulamiento object at 0x001BE718>



''' el prefijo __ para crear un atributo y un método privados en la clase Encapsulamiento. Eso es una forma de aplicar el principio de encapsulamiento en Python, que consiste en ocultar los detalles de implementación de una clase y solo exponer los métodos y atributos públicos . Con el prefijo __, se evita que se pueda acceder o modificar el atributo o el método desde fuera de la clase . Para poder acceder a ellos, se deben crear métodos públicos que los devuelvan o los llamen'''