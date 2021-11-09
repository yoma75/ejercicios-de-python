# Pedir un codigo y una contraseña al usuario, no se le dejara proseguir hasta qe el codigo sea 1234 y la clave sea 5000

codigo = "1234"
clave = "5000"

cont = 0

conectado = bool;
while cont < 3:
    cod = input("ingrese código: ");
    cla = input("ingrese contraseña: ");
    if cod == codigo and cla == clave:
        print ("Bienvenido al sistema\n")
        conectado = True
        break
    else:
        cont = cont + 1;
        print ("Usuario y contraseña incorrecta\n")
        conectado = False

