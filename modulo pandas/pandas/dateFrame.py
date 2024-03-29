'''Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:'''
    # Mes     ventas      gastos
    # Enero   78000       8767

import pandas as pd 

datos = {
    'Mes':['Enero','Febrero','Marzo','Abril'], 
    'Ventas':[30500, 35600, 28300, 33900], 
    'Gastos':[22000, 23400, 18100, 20700]
}

contabilidad = pd.DataFrame(datos)

print(f'\n{contabilidad}')

#        Mes  Ventas  Gastos
# 0    Enero   30500   22000
# 1  Febrero   35600   23400
# 2    Marzo   28300   18100
# 3    Abril   33900   20700