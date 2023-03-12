''' Escribir una clase que se llame Areas(). A partir de un constructor se deben pasar los valores de Base y Altura. Luego, se debe calcular area de un cuadrado, triangulo y pentágono '''


# Importar el módulo math para usar la función tan
import math

# Definir la clase Areas
class Areas:

  # Inicializar los atributos base y altura
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  # Calcular el área de un cuadrado
    def area_cuadrado(self):
      return self.base * self.altura

  # Calcular el área de un triángulo
  def area_triangulo(self):
    return (self.base * self.altura) / 2

  # Calcular el área de un pentágono regular
  def area_pentagono(self):
  
  # Calcular la apotema usando la fórmula a = s / (2 · tan(π/5))
    s = self.base  # La base es igual a la longitud de un lado del pentágono
    a = s / (2 * math.tan(math.pi / 5))
        
  # Usar la fórmula A = (5/2) · s · a
    return (5/2) * s * a


# Crear un objeto de la clase Areas con una base de 10 y una altura de 8
areas1 = Areas(10, 8)

# Imprimir los resultados de los métodos de la clase Areas
print(f"El área del cuadrado es {areas1.area_cuadrado()} cm²")
print(f"El área del triángulo es {areas1.area_triangulo()} cm²")
print(f"El área del pentágono es {areas1.area_pentagono()} cm²")
