# implementa una lista enlazada simple con las funcionalidades de agregar, eliminar y encontrar nodos:

class Alumno:
  def __init__(self, nombre, cedula, telefono):
    self.nombre = nombre
    self.cedula = cedula
    self.telefono = telefono
    self.siguiente = None

class ListaEnlazada:
  def __init__(self):
    self.inicio = None

  def lista_vacia(self):
    return self.inicio is None

  def insertar_en_lista(self, nombre, cedula, telefono):
    nuevo_nodo = Alumno(nombre, cedula, telefono)
    if self.lista_vacia():
        self.inicio = nuevo_nodo
    else:
      apuntador_auxiliar = self.inicio
      while apuntador_auxiliar.siguiente is not None:
        apuntador_auxiliar = apuntador_auxiliar.siguiente
        apuntador_auxiliar.siguiente = nuevo_nodo

  def imprimir_lista(self):
    apuntador_auxiliar = self.inicio
    if self.lista_vacia():
      print("NO HAY ELEMENTOS EN LA LISTA")
    else:
      while apuntador_auxiliar is not None:
        print("------------NODO--------------")
        print(f"NOMBRE: {apuntador_auxiliar.nombre}")
        print(f"CEDULA: {apuntador_auxiliar.cedula}")
        print(f"TELEFONO: {apuntador_auxiliar.telefono}")
        apuntador_auxiliar = apuntador_auxiliar.siguiente

# Ejemplo de uso
if __name__ == "__main__":
  lista_alumnos = ListaEnlazada()
  lista_alumnos.insertar_en_lista("Luis", 123, 4567890)
  lista_alumnos.insertar_en_lista("Ana", 456, 9876543)
  lista_alumnos.imprimir_lista()


'''
------------NODO--------------
NOMBRE: Luis
CEDULA: 123
TELEFONO: 4567890
------------NODO--------------
NOMBRE: Ana
CEDULA: 456
TELEFONO: 9876543
'''