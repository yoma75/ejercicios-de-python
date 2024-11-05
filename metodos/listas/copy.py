# COPY: crea una copia de la lista especificada
frutas = ['manzana', 'banana', 'cerezas']
x = frutas.copy()
print(x)


# Otra forma de copiar es con el metodo: LIST
marcasAutos = ['mercedez', 'audi', 'renault']
marcasCopia = list(marcasAutos)
print(marcasCopia)


# Tambien se puede hacer una copia con el OPERADOR SLICE ':'
marcasAutos = ['mercedez', 'audi', 'renault']
copiaAutos = marcasAutos[:]
print(copiaAutos)  # ['mercedez', 'audi', 'renault']

