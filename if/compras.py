# Programa que permita calcular el valor final a pagar en una súper tienda en donde se aplican los siguientes descuentos: a) Por compras entre 10.000 y 20.000 el 10% b) Por compras entre 20.001 y 50.000 el 30% c) Por compras superiores a 50.000 el 50%

print('')
valor_a_pagar = int(input('Valor de su compra: '))

if valor_a_pagar >= 10000 and valor_a_pagar <= 20000:
    descuento1 = (valor_a_pagar * 10) / 100
    total = valor_a_pagar - descuento1
    print('Ha recibido un descuento del "10%" en su compra')
    print(f'Total: {total}'.upper())

elif valor_a_pagar >= 20001 and valor_a_pagar <= 50000:
    descuento2 = (valor_a_pagar * 30) / 100
    total = valor_a_pagar - descuento2
    print('Ha recibido un descuento del "30%" en su compra')
    print(f'Total: {total}'.upper())
    
elif valor_a_pagar >= 50001:
    descuento3 = (valor_a_pagar * 50) / 100
    total = valor_a_pagar - descuento3
    print('Ha recibido un descuento del "50%" en su compra')
    print(f'Total: {total}'.upper())
else:
    print('No recibe descuento, compra menor a 10.000')