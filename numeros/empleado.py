# Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = float(input('Numero de horas trabajadas: '))
costo_hora = float(input('Valor de la hora: '))

total = round(horas * costo_hora,3)
print('Valor a pagar: {}'.format(total))

