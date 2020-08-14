# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print(' Pizzería Bella Napoli '.upper().center(90,'-'))
print('')


print('1. VEGETARIANA: pimiento, tofu, mozzarella y tomate'.center(70))
print('2. NO VEGETARIANA: peperoni, jamon, salmon, mozzarella y tomate'.center(82))
print('')

pedido = int(input('Digite el numero de pizza que desea pedir: '))
print('')
if pedido == 1:
    print('Usted eligio la pizza vegetariana')
else:
    print('Usted eligio la pizza NO vegetariana')


