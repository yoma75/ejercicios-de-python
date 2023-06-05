'''Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:'''
    # Mes     ventas      gastos
    # Enero   78000       8767

import pandas as pd

datos = [['Enero', 30500, 22000], 
         ['Febrero', 35600, 23400], 
         ['Marzo', 28300, 18100], 
         ['Abril', 33900,20700]]

contabilidad = pd.DataFrame(datos, columns=['Mes', 'Ventas', 'Gastos'])

print(f'\n{contabilidad}')

#        Mes  Ventas  Gastos
# 0    Enero   30500   22000
# 1  Febrero   35600   23400
# 2    Marzo   28300   18100
# 3    Abril   33900   20700
