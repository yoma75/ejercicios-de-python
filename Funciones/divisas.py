# Conversor de moneda:

menu = """ 
Bienvenido al conversor de monedas  

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion:  """

opcion = int(input(menu))

def conversion():
    pesos = float(input('Cuantos pesos tienes: '))
    valor_dolar = 3875  # 3875: valor dolar
    dolares = round(pesos / valor_dolar, 2)
    print(f'{pesos} pesos equivalen a {dolares} dolares')

if opcion == 1:
    valor_dolar = 3660
    conversion()
elif opcion == 2:
    valor_dolar = 70.66
    conversion()
elif opcion == 3:
    valor_dolar = 22.39
    conversion()
else:
    print('Opcion incorrecta')


