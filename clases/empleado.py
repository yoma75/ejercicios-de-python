# Clase padre o super clase
class Empleado:
  def __init__(self, nombre, edad, legajo, sueldo):
    self.nombre = nombre
    self.edad = edad
    self.legajo = legajo
    self.sueldoBase = sueldo
  
  def calcularSueldo(self, descuentos, bonos):
    return self.sueldoBase - descuentos + bonos


# Clase hija o subclase, hereda los metodos __init__ de su padre (class Empleado)
class AgenteVentas(Empleado):
  def __init__(self, nombre, edad, legajo, sueldo, mostrador):
      self.numeroMostrador = mostrador
      super().__init__(nombre, edad, legajo, sueldo)  # se llama a la clase padre con super()


# Crear una instancia:
pedro = AgenteVentas('Pedro Sarmiento', 32, 'A120', 55000, 4)
print(pedro.nombre, pedro.sueldoBase)  # Pedro Sarmiento 55000
print(pedro.calcularSueldo(100, 3000))  # 57900 (55000 - 100 + 3000) sueldoBase - descuentos + bonos


# Clase hija
class Tripulante(Empleado):
  



      