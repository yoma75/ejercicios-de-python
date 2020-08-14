# Calcular la Diferencia en Días de Dos Fechas Dadas

from datetime import date

# date: guarda elemento tipo fecha
hoy = date(2020, 6, 2)
otra_fecha = date(2023, 2, 13)

diferencia = otra_fecha - hoy

# .days: (atributo) solo me muestra los dias
print()
print(f'La diferencia es de: {diferencia.days} dias'.upper())

