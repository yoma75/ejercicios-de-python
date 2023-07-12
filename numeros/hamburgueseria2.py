import math

HAMB_POLLO = 5500
HAMB_CARNE = 7400
HAMB_PESCADO = 6000
GASEOSA = 2200
IVA = 0.19

acumuladores = {'pollo': 0, 'carne': 0, 'pescado': 0, 'gaseosa': 0}
totales = {'pollo': 0, 'carne': 0, 'pescado': 0, 'gaseosa': 0}

while True:
    menu = """
        \n***** BIENVENIDOS A LA HAMBURGUESERIA *****\n
        1. Hamburguesa de pollo
        2. Hamburguesa de carne
        3. Hamburguesa de pescado
        4. Gaseosa
        5. Salir

        \nElige una opción: """
    
    opcion = int(input(menu))

    if opcion == 5:
        print('GRACIAS POR SU COMPRA')
        break

    elif opcion in range(1, 5):
        cantidad = int(input(f'Cuantas {"hamburguesas de pollo" if opcion == 1 else "hamburguesas de carne" if opcion == 2 else "hamburguesas de pescado" if opcion == 3 else "gaseosas"} desea: '))
        tipo = 'pollo' if opcion == 1 else 'carne' if opcion == 2 else 'pescado' if opcion == 3 else 'gaseosa'
        totales[tipo] = cantidad * (HAMB_POLLO if tipo == 'pollo' else HAMB_CARNE if tipo == 'carne' else HAMB_PESCADO if tipo == 'pescado' else GASEOSA)
        acumuladores[tipo] += cantidad

valor_neto = sum(totales.values())
con_iva = valor_neto * IVA
total_pagar = math.ceil(valor_neto + con_iva)

if valor_neto >= 2200:
    print('\n--- Usted compró lo siguiente: ---')
    print('************************************')

    for tipo, cantidad in acumuladores.items():
        if cantidad >= 1:
            print(f'{cantidad} Hamburguesas de {tipo} a ${HAMB_POLLO if tipo == "pollo" else HAMB_CARNE if tipo == "carne" else HAMB_PESCADO if tipo == "pescado" else GASEOSA} c/u = {totales[tipo]}')

    print(f'\nSubtotal: ${valor_neto}')
    print(f'IVA: ${con_iva}')
    print(f'Total a pagar: ${total_pagar}'.upper())

    paga = int(input('\nCancela con efectivo: $ '))
    cambio = paga - total_pagar
    print(f'Su cambio es: ${round(cambio)}\n')

else:
    print('No eligió ninguna opción')
