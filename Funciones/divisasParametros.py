def conversor(tipo_pesos, valor_dolar):
    pesos = float(input(f'Cuantos pesos {tipo_pesos} tienes: '))
    dolares = round(pesos / valor_dolar, 2)
    print(f'{pesos} pesos {tipo_pesos} equivalen a {dolares} dolares'.upper())

menu = """ 
Bienvenido al conversor de monedas  

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion:  """

opcion = int(input(menu))

if opcion == 1:
    conversor('colombianos', 3875)
elif opcion == 2:
    conversor('argentinos', 65)
elif opcion == 3:
    conversor('mexicanos', 24)
else:
    print('Esta opcion no existe')
