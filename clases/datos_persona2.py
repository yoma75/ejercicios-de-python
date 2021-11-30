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
