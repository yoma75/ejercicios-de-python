# Decir cuantos dias tiene el mes que digite el usuario:

# Introduce el nombre de un mes: febrero
# febrero tiene 28/29 días

# Introduce el nombre de un mes: marzo
# marzo tiene 31 días

# Introduce el nombre de un mes: abril
# abril tiene 30 días*/

mes = input('Escriba el mes: '.upper())

if mes == 'febrero':
    print(f'El mes de {mes} tiene 28 dias')
elif mes=='enero' or mes=='marzo' or mes=='mayo' or mes=='julio' or mes=='octubre' or mes=='agosto' or mes=='diciembre':
    print(f'El mes de {mes} tiene 31 dias')
elif mes=='abril' or mes=='jumio' or mes=='septiembre' or mes=='noviembre':
    print(f'El mes de {mes} tiene 30 dias')
else:
    print('Este mes no existe')