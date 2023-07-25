# copy: crea una copia independiente de un objeto, en lugar de una referencia a la misma ubicación de memoria. 
# La copia NO DEBE verse afectada por los cambios realizados en el array original

import numpy as np

arr_original = np.array([1, 2, 3, 4, 5])

copia = arr_original.copy()
arr_original[0] = 42

print(arr_original)  # [42  2  3  4  5]
print(copia)         # [1 2 3 4 5]


# ---------------------------------------------------------------------------------------------------------

# View: afecta el array original y la copia

arr = np.array([1, 2, 3, 4, 5])

copia = arr.view()
arr[0] = 42

print(arr)    # [42  2  3  4  5]
print(copia)  # [42  2  3  4  5]


# ---------------------------------------------------------------------------------------------------------

# base: se utiliza para determinar si un array es una vista (view) de otro array o si es una copia independiente (deep copy). Este atributo es una propiedad de los objetos array en NumPy que puede ser útil para comprender cómo se están manipulando los datos y si los cambios realizados en un array afectarán a otros.

'''En el ejemplo siguiente, se utilizan dos métodos diferentes para copiar un array: copy() y view(). Ambos métodos generan un nuevo array, pero tienen comportamientos ligeramente diferentes con respecto a su relación con el array original. 

copy(): Este método crea una copia profunda (deep copy) del array original, lo que significa que se crea un nuevo array independiente con sus propios datos y cualquier cambio realizado en el nuevo array no afectará al original. El atributo base de un array creado mediante copy() es None, ya que no está vinculado a ningún array original.

view(): En cambio, view() crea una vista (view) del array original. Una vista es un nuevo objeto array que apunta a los mismos datos que el array original. Esto significa que los cambios realizados en la vista también afectarán al array original y viceversa. En este caso, el atributo base de la vista apuntará al array original.

En conclusion: copy() crea un nuevo array independiente y view() crea un nuevo objeto array que apunta a los mismos datos que el original
'''


arr = np.array([1, 2, 3, 4, 5])

# Crear una copia profunda del array original
x = arr.copy()

# Crear una vista del array original
y = arr.view()

print(x.base)  # None ('x' es una copia independiente)
print(y.base)  # [1 2 3 4 5] ('y' es una vista del array original)
