# difference: retorna un conjunto que contiene los items que solo existen en el conjunto 'x', y no en el conjunto 'y':

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(z)  #{'banana', 'cherry'}

