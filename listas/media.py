TAM = 6
numero = list([])
restdiv, valor1, valor2 = 0,0,0

# Genera 6 vueltas
for x in range(TAM):
    valor = float(input("Ingrese un valor entero: "))
    numero.append(valor)

print()

valor1 = (numero[0]+numero[2]+numero[4])/3
valor2 = (numero[1]+numero[3]+numero[5])/3
restdiv = (numero[0]%numero[5])

print(f'La media de los numeros {numero[0]}, {numero[2]} y {numero[4]} es: {valor1}')
print(f'La media de los numeros {numero[1]}, {numero[3]} y {numero[5]} es: {valor2}')
print(f'El resto de la division de {numero[5]} y {numero[0]} es: {restdiv}')

