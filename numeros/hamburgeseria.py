

HAMB_POLLO = 5500
HAMB_CARNE = 7400
HAMB_PESCADO = 6000
GASEOSA = 2200
IVA = 0.19

menu = 0
acumulador_hpollo = 0
acumulador_hcarne = 0
acumulador_hpescado = 0
acumulador_gaseosa = 0

while(menu != 5):

    menu = """
        \n***** BIENVENIDOS  A LA HAMBURGUESERIA *****\n
        1. Hamburguesa de pollo
        2. Hamburguesa de carne
        3. Hamburguesa de pescado
        4. Gaseosa
        5. Salir

        \nElige una opcion: """
    
    opcion = int(input(menu))

    if opcion == 1:
        cantidad_hamburguesa_pollo =  int(input('Cuantas hamburguesas de pollo desea: '))
        total_hamburguesa_pollo = HAMB_POLLO * cantidad_hamburguesa_pollo
        acumulador_hpollo += cantidad_hamburguesa_pollo

    elif opcion == 2:
        cantidad_hamburguesa_carne = int(
        input('Cuantas hamburguesas de carne desea: '))
        total_hamburguesa_carne = HAMB_CARNE * cantidad_hamburguesa_carne
        acumulador_hcarne += cantidad_hamburguesa_carne

    elif opcion == 3:
        cantidad_hamburguesa_pescado = int(
        input(' Cuantas hamburguesas de pescado desea: '))
        total_hamburgesa_pescado = HAMB_PESCADO * cantidad_hamburguesa_pescado
        acumulador_hpescado += cantidad_hamburguesa_pescado

    elif opcion == 4:
        cantidad_gaseosa = int(input('Cuantas gaseosas desea: '))
        if cantidad_gaseosa == 0 or cantidad_gaseosa != 9999:
            total_gaseosa = GASEOSA * cantidad_gaseosa
            acumulador_gaseosa += cantidad_gaseosa

    else:
        print('GRACIAS POR SU COMPRA')
        break

valor_neto = total_hamburguesa_pollo + total_hamburguesa_carne + total_hamburgesa_pescado + total_gaseosa
con_iva = valor_neto * IVA
total_pagar = valor_neto + con_iva

print('\nUsted compro lo siguiente:')
print(f'{acumulador_hpollo} Hamburguesas de pollo a $ 5500 c/u = {total_hamburguesa_pollo}')
print(f'{acumulador_hcarne} Hamburguesas de carne a $ 7400 c/u = {total_hamburguesa_carne}')
print(f'{acumulador_hpescado} Hamburguesas de pescado a $ 6000 c/u = {total_hamburgesa_pescado}')
print(f'{acumulador_gaseosa} Gaseosas a $ 2200 c/u = {total_gaseosa}')

print(f'\nSubtotal: $ {valor_neto}')
print(f'IVA: $ {con_iva}')
print(f'Total a pagar: $ {total_pagar}'.upper())

paga = int(input('\nCancela con: $ '))
cambio = paga - total_pagar

print(f'Su cambio es: $ {cambio}')







