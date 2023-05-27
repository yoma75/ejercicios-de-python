candidatos = {
    'A': 'rojo',
    'B': 'verde',
    'C': 'azul'
}

opcion = input("Elija su candidato (A, B o C): ").upper()

if opcion in candidatos:
    print("Usted ha votado por el partido", candidatos[opcion])
else:
    print("Opción errónea")
