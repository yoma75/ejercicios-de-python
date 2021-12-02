# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

# self.sumita, self.restica, self.multiplicacion, self.dividir: son variables


class Calculadora:
  def __init__(self):  # metodo constructor
    self.valor1 = int(input('\nIngrese el primer valor: '))
    self.valor2 = int(input('Ingrese el segundo valor: '))


  def suma(self):
    self.sumita = self.valor1 + self.valor2
    print(f'\nEl total de la SUMA es: {self.sumita}')


  def resta(self):
    self.restica = self.valor1 - self.valor2
    print(f'El total de la RESTA es: {self.restica}')
  

  def multiplicar(self):
    self.multiplicacion = self.valor1 * self.valor2
    print(f'El total de la MULTIPLICACION es: {self.multiplicacion}')


  def division(self):
    self.dividir = self.valor1 / self.valor2
    print(f'El total de la DIVISION es: {self.dividir}\n')


calcular = Calculadora()

calcular.suma()
calcular.resta()
calcular.multiplicar()
calcular.division()

