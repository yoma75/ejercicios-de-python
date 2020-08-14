# Gramage y valor de producto

nombreProducto = input('Nombre del producto: ')
pesoProducto = float(input('Peso total del producto en libras: '))
valor_total = float(input('Valor total del producto: '))
print()
newProductPeso = float(input('Nuevo Peso total del producto en gramos: '))

gramos = round(pesoProducto * 500) # 500 gramos tiene una libra
valorLibra = round(valor_total / pesoProducto)
valorGramo = round(valorLibra / 500) 
verifica = round(valorGramo * gramos)
nuevoProductopeso = newProductPeso * valorGramo

# Si el valor de la libra es mayor a 800 subir su precio a 1000, diferencia 200
if valorLibra >= 800:
    nuevovalorLibra = 0
    nuevovalorLibra = valorLibra + 200

gananciaXlibra = (nuevovalorLibra - valorLibra) * pesoProducto

print()
print(f'{nombreProducto} pesa {gramos} gramos'.upper())
print(f'Valor por libra: {valorLibra} '.upper())
print(f'Nuevo valor por libra: {nuevovalorLibra} '.upper())
print(f'Valor por gramo: {valorGramo} '.upper())
print(f'Verifica valor total del producto: {verifica} '.upper())
print(f'Ganancia total por libra es de: {gananciaXlibra} pesos'.upper())
print(f'Cuanto vale {newProductPeso} gramos: {nuevoProductopeso} pesos'.upper())
