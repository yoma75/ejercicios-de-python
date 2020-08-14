#  Programa que permita determinar el salario a pagar a un empleado teniendo como entradas el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud

salario = int(input('Salario del trabajador: '))
dias = int(input('Numero de dias trabajados: '))
total = (salario * dias)
salud = (total * 15) / 100
pension = (total * 10) / 100

print('')
print(f'Su sueldo total es de: $ {total}')
print(f'Menos el 15% de salud: {salud}')
print(f'Menos el 10% de pension: {pension}')
print('')

print(f'Total a pagar: $ {total-salud-pension}'.upper())

