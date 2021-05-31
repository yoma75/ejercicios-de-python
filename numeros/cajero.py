# -*- coding: utf-8 -*-
import random
usuario = "789"
passw = "123"
saldo = random.randint(0,1000000)
saldo2 = random.randint(0,50000)
cont = 0

conectado = bool;
while cont < 3:
    us = input("ingrese rut: ");
    co = input("ingrese contraseña: ");
    if us == usuario and passw == co:
        print ("Bienvenido al sistema")
        conectado = True
        break
    else:
        cont = cont + 1;
        print ("Usuario y contraseña incorrecta")
        conectado = False

while conectado == True:
    print ("Que operacion desea utilizar?:")
    print ("1.- Giro")
    print ("2.- Deposito")
    print ("3.- Traspaso")
    print ("4.- Consulta Saldo")
    print ("0.- Para cerrar")
    opcion  = int(input("Ingrese opcion: "))

    if opcion  == 1:
        monto = int(input("Ingrese monto a girar: "))    
        saldo = saldo - monto
        print (f"ha retirado {monto}")

    elif opcion == 2:
        monto = int(input("Ingrese monto a Depositar: "))          
        saldo = saldo + monto
        print (f"su nuevo saldo es {saldo}")

    elif opcion == 3:
        cu2 = input("Ingrese cuenta a depositar ")    
        monto = int(input("Ingrese monto a Transferir: "))
        saldo = saldo - monto
        saldo2 = saldo2 + monto
        print (f'se han transferido {monto} pesos a la cuenta {cu2}')
        print (f"el nuevo saldo es: {saldo2}")

    elif opcion == 4:
        print (f"Su saldo es: {saldo}")

    elif opcion == 0:
        break