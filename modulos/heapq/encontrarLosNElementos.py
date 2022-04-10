# Cómo Encontrar los n Elementos Más Grandes o Más Pequeños de una Lista con heapq

import heapq

numeros = [54, 69, 78, 96, 32, 10, 54, 23, 102]


# 2 valores mas grandes de la lista
print(heapq.nlargest(2, numeros))  # [102, 96]


# 4 valores mas pequeños de la lista
print(heapq.nsmallest(4, numeros))  # [10, 23, 32, 54]

