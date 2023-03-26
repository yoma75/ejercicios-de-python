# Desarrollado con chatGPT: en el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra

paises = {"Guatemala": "Ciudad de Guatemala",
          "El Salvador": "San Salvador",
          "Honduras": "Honduras",
          "Nicaragua": "Managua",
          "Costa Rica": "San Jose",
          "Panama": "Panama",
          "Argentina": "Buenos Aires",
          "Colombia": "Bogota",
          "Venezuela": "Caracas",
          "España": "Madrid"
          }

pais = input("\nIngrese un país: ")
capital = paises.get(pais)  # GET: Return the value for key if key is in the dictionary, else default

if capital:
    print(f"La capital de {pais} es {capital}\n")
else:
    print(f"Lo siento, no se encontró el país {pais}\n")

