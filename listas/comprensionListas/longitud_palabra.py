# Transformación de cadenas: Supongamos que tienes una lista de palabras y quieres crear una nueva lista que contenga la longitud de cada palabra en la lista original. Puedes usar la comprensión de listas para aplicar la función len() a cada palabra:

# nueva_lista = [expresion for elemento in lista_existente]

palabras = ["hola", "mundo", "python", "programación"]
longitudes = [len(x) for x in palabras]

print(longitudes)  # [4, 5, 6, 12]
