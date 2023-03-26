'''Este código crea una clase llamada "Cajero" que tiene tres métodos: depositar, retirar y consultar_saldo. Cada uno de estos métodos realiza la operación correspondiente y muestra el saldo actual. En el método principal, se crea una instancia del cajero con un saldo inicial de 1000 y se inicia un bucle que permite al usuario realizar una operación a la vez hasta que elija la opción "4" para salir.'''

class Cajero:

  # Se define la clase 'Cajero con un constructor que recibe un parámetro 'saldo' y lo asigna como atributo de instancia 'self.saldo
  def __init__(self, saldo):
    self.saldo = saldo

  # Metodo depositar
  def depositar(self, cantidad):
    self.saldo += cantidad
    print("Depósito realizado. Saldo actual:", self.saldo)

  # Metodo retirar
  def retirar(self, cantidad):
    if cantidad <= self.saldo:
      self.saldo -= cantidad
      print("Retiro realizado. Saldo actual:", self.saldo)
    else:
      print("Saldo insuficiente")

  # Metodo consultar saldo
  def consultar_saldo(self):
    print("Saldo actual:", self.saldo)


# Este bloque de código es el punto de entrada del programa
if __name__ == "__main__":
    cajero = Cajero(1000)

    while True:
      print("\n¿Qué operación desea realizar?")
      print("1. Depositar")
      print("2. Retirar")
      print("3. Consultar saldo")
      print("4. Salir")

      opcion = int(input("Ingrese una opción: "))

      if opcion == 1:
          cantidad = float(input("Ingrese la cantidad a depositar: "))
          cajero.depositar(cantidad)

      elif opcion == 2:
          cantidad = float(input("Ingrese la cantidad a retirar: "))
          cajero.retirar(cantidad)

      elif opcion == 3:
          cajero.consultar_saldo()

      elif opcion == 4:
        break
      else:
        print("Opción inválida")
