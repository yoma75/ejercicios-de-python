num1 = int(input('Digite un numero: '))
num2 = int(input('Digite otro numero: '))

print("----------- Calculadora -----------")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
opc = int(input('Digite una opcion: '))
print("-----------------------------------")

if opc == 1:
    suma = (num1 + num2)    
    print("La suma entre {0} y {1} es: {2}".format(num1,num2,suma))

elif opc == 2:
    resta = (num1 - num2)
    print("La resta entre {0} y {1} es: {2}".format(num1,num2,resta))
    
elif opc == 3:
    multi =(num1 * num2)
    print("La multiplicacion entre {0} y {1} es: {2}".format(num1,num2,multi))
    
elif opc == 4:
    divi = (num1 // num2)
    print(f'La division entre {num1} y {num2} es: {divi}')

elif opc >= 5:
    print('Opcion errada')
 



