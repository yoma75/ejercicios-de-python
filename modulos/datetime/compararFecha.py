from datetime import datetime, timedelta

# imprime la fecha de hoy
fecha_hoy = datetime.now()
print(f'\nLa fecha y hora de hoy es: {fecha_hoy}')


# imprime la fecha de ayer
# timedelta: sirve para agregar o quitar días o semanas a una fecha
un_dia = timedelta(days=1)
ayer = fecha_hoy - un_dia
print(f'\nAyer fue: {str(ayer)}')


# pedirle al usuario que ingrese una fecha
nueva_fecha = input(f'\nPor favor digite una fecha (dd/mm/yyyy): ')
nueva_fecha = datetime.strptime(nueva_fecha, '%d/%m/%Y')


# imprima la fecha una semana después de la fecha ingresada
una_semana = timedelta(weeks=1)
una_semana_despues = nueva_fecha + una_semana
print(f'\nUna semana después será: {str(una_semana_despues)}')

