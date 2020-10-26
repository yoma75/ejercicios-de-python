# Dada una lista de números enteros, devuelve la diferencia entre los números enteros más grandes y más pequeños de la lista.

# diferencia([10, 15, 20, 2, 10, 6]) ➞ 18
# 20 - 2 = 18

def diferencia(listica):
    a = max(listica)
    b = min(listica)
    x = a - b
    
    return print(f'\n{a} - {b} = {x}')

diferencia([10, 15, 20, 2, 10, 6]) # 20 - 2 = 18
diferencia([23, 56, 98, 1, 29, 8]) # 98 - 1 = 97
diferencia([300, 490, 134, 638, 740, 628]) # 740 - 134 = 606

