'''POW: devuelve un valor elevado a una determinada potencia'''

def potencia(valor, elevado):
    numero = pow(valor, elevado)
    print(numero)

potencia(5,3)  # 125: 5 * 5 * 5
potencia(2,6)  # 64
potencia(15,4)  # 50625

