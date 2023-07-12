# Calcular el salario semanal de un trabajador, el salario se calcula en base a las horas semanales trabajadas y de acuerdo a un precio especificado por cada hora. Si se pasa de 40 horas trabajadas, las horas extraordinarias se pagaran a razon de 1.5 veces la hora ordinaria.

def calcular_salario():
    nombre = input('Nombre del trabajador: ')
    horas_trabajadas = int(input('Digite el numero de horas trabajadas: '))
    precio_hora = int(input('Digite el precio de la hora: '))

    if horas_trabajadas <= 40:
        salario = (horas_trabajadas * precio_hora)        
    else:
        salario = int(40 * precio_hora + 1.5 * precio_hora * (horas_trabajadas - 40))
    
    impuestos = int(0.19 * salario)
    neto = salario - impuestos

    print(f'\nEl salario de {nombre} es de $ {salario} \nmenos impuestos $ {impuestos} \nvalor neto a pagar: $ {neto}\n')

calcular_salario()
