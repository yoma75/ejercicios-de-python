# Conversor de divisas:

menu = """ 
Bienvenido al conversor de monedas  

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:  """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input('Cuantos pesos Colombianos tienes: '))
    valor_dolar = 3875
    dolares = round(pesos / valor_dolar, 2)
    print(f'{pesos} pesos colombianos equivalen a {dolares} dolares')

elif opcion == 2:
    pesos = float(input('Cuantos pesos Argentinos tienes: '))
    valor_dolar = 65
    dolares = round(pesos / valor_dolar, 2)
    print(f'{pesos} pesos argentinos equivalen a {dolares} dolares')
    
elif opcion == 3:
    pesos = float(input('Cuantos pesos Mexicanos tienes: '))
    valor_dolar = 24
    dolares = round(pesos / valor_dolar, 2)
    print(f'{pesos} pesos mexicanos equivalen a {dolares} dolares')
else:
    print('Ingrese una opcion correcta')
