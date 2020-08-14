# Mostar el precio del IVA de un producto con un valor de $ 100.000 y su preci0o final

IVA = 0.19

precioProducto = int(input('Digite el valor del producto: '))
precioIva = precioProducto * IVA

otro = precioIva+precioProducto

print('El valor del producto con el IVA es de: $'+str(precioIva))
print('El valor final es: $ '+str(precioIva+precioProducto))


print('El resultado es {r:1.2f}'.format(r=otro))