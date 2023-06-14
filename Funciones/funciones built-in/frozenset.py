# frozenset: congela una lista y la hace inmutable
# Si intenta cambiar el valor de un elemento congelado este provocará un error

frutas = ['manzana', 'guama', 'mamoncillo']
x = frozenset(frutas)

print(x)  # frozenset({'guama', 'mamoncillo', 'manzana'})
