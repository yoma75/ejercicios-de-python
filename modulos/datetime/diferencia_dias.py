# Calcular la diferencia en días de dos Fechas dadas

from datetime import date

def diferenciaDias(year, month, days):
    # date: guarda elemento tipo fecha
    today = date(year, month, days)
    otra_fecha = date(2050, 2, 13)

    diferencia = otra_fecha - today
    return print(f'\nLa diferencia es de: {diferencia.days} dias'.upper())
    # .days: (atributo) solo me muestra los dias

diferenciaDias(2019, 12, 30)
diferenciaDias(2045, 9, 19)
diferenciaDias(2020, 10, 26)

