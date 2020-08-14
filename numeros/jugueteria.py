# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

PAYASITO = 112
MUÑECA = 75

numero_payasos = int(input('Numero de payasos vendidos: '))
numero_muñecas = int(input('Numero de muñecas vendidas: '))

peso_total = (PAYASITO*numero_payasos + MUÑECA*numero_muñecas)
print('El peso total del paquete es de {} gramos'.format(peso_total))

