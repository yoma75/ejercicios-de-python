# Crear una Clase para Representar los Datos de una Persona
# Este es el método mas corto para crear la clase del ejemplo anterior (datos_persona2) referente a persona

from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
    correo: str

def __str__(self) -> str:
    return (f'{self.nombre}: {self.edad}, {self.correo}')

personita1 = Persona('Carlos Ramírez', 34, 'micorreo@hotmail.com')

print(personita1)  # Persona(nombre='Carlos Ramírez', edad=34, correo='micorreo@hotmail.com')
print(personita1.edad)  # 34



'''la librería dataclasses para crear una clase Persona con un decorador @dataclass. Eso es una forma alternativa y más simple de crear clases en Python 3.7 o superior . Con el decorador @dataclass, no necesitas definir el método especial __init__ ni el método __str__, ya que se generan automáticamente . También puedes usar otros parámetros en el decorador para modificar el comportamiento de la clase, como frozen, order o eq '''
