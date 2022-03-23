# . Programa que muestre en pantalla los múltiplos de 3 y de 5 teniendo como límite el número 36 y 99. 

for x in range(36, 100):
    if x % 3 == 0:
        print(f'{x} .... Es múltiplo de 3')
    elif x % 5 == 0:
        print(f'{x} .... Es múltiplo de 5')

