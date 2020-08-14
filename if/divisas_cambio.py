# Cambio de pesos colombianos a dolares e inverso:

DOLAR = 4530
COLOMBIA = 2300

print('-------- cambio de divisas ---------'.upper())
print('1. De pesos colombianos a dolares')
print('2. De dolar americano a pesos colombianos')

print('')
opc= int(input('Digita tu opcion: '))

if opc == 1:
    pesoColom = int(input('Digite el valor en pesos Colombianos: '))
    cambio1 = float(pesoColom // DOLAR)
    print('{} pesos Colombianos equivalen a: {r:1.2f} dolares'.format(pesoColom,r=cambio1))
elif opc == 2: 
    dolarsito = int(input('Digite el valor en dolares americanos: '))
    cambio2 = (dolarsito * COLOMBIA)
    print(f'{dolarsito} dolares americanos equivalen a: {cambio2} pesos Colombianos')
else:
    print('Error esa opcion no existe')
