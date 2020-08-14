# Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA

IVA = 16
print('')
print('........... tienda el mejor .............'.upper())
print('')

valor_unitario = int(input('Valor unitario del producto: $ '))
cantidad_productos = int(input('Cantidad de productos: '))
valor = (valor_unitario * cantidad_productos)
valor_con_iva = (valor * IVA) // 100

print('')
print(f'El subtotal es de: {valor}')
print(f'Mas el IVA: {valor_con_iva}')
print('')
print(f'Total: {valor_con_iva+valor}'.upper())

