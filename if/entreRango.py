# Decir entre que rango esta el numero que entra por teclado:

num = int(input('Digita un numero positivo entre uno y cincuenta: '))

if num >= 1 and num <= 10:
    print('El numero {} esta entre el rango de 1 y 10'.format(num))

elif num >= 11 and num <= 20:
     print('El numero {} esta entre el rango de 11 y 20'.format(num))

elif num >= 21 and num <= 30:
     print('El numero {} esta entre el rango de 21 y 30'.format(num))

elif num >= 31 and num <= 40:
     print('El numero {} esta entre el rango de 31 y 40'.format(num))

elif num >= 41 and num <= 50:
     print('El numero {} esta entre el rango de 41 y 50'.format(num))

else:
    print('Esta fuera del rango')

