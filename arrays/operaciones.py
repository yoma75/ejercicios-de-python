import numpy as np

array1 = np.array([1,2,3,4])
print(array1 * 7)  # [ 7 14 21 28]

array1 += 5
print(array1)  # [6 7 8 9]

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista1,lista2)
array_doble = np.array(lista_doble)
print(array_doble / 2)  # [[0.5 1.  1.5 2. ]
                        # [2.5 3.  3.5 4. ]]



