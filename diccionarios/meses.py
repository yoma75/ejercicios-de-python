# Pide al usuario el nombre de un mes y responde cuántos días tiene (suponiendo un año no bisiesto)

dias = {
    "enero": 31,
    "febrero": 28, 
    "marzo": 31, 
    "abril": 30,
    "mayo": 31, 
    "junio": 30, 
    "julio": 31, 
    "agosto": 31,
    "septiembre" : 30, 
    "octubre": 31, 
    "noviembre": 30, 
    "diciembre": 31
}

nombreMes = input("Dime el nombre del mes: ")
print("Tiene", dias[nombreMes], "dias" )