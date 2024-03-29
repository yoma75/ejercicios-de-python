'''En este desafío, un granjero te pide que le digas cuántas patas se pueden contar entre todos sus animales. El agricultor cría tres especies:
        
chickens = 2 patas
cows = 4 patas
pigs = 4 patas
        
El granjero ha contado sus animales y te da un subtotal para cada especie. Tienes que implementar una función que devuelva el número total de patas de todos los animales.

animals(2, 3, 5) ➞ 36'''

def animals(ch, c, p):
    chicken, cow, pig = 2, 4, 4
    suma = ((ch * chicken) + (c * cow) + (p * pig))
    return print(f'\nTotal: {suma} patas')

animals(2, 3, 5)  # Total: 36 patas
animals(2, 2, 1)  # Total: 16 patas

