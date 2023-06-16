# slice: se utiliza para especificar cómo dividir una secuencia. 
# slice(start, end, step)

letras = ("h", "b", "c", "d", "p", "f", "g", "h")
x = slice(3, 5)
print(letras[x])  # ('d', 'p')

x = slice(0, 8, 3)
print(letras[x])  # ('h', 'd', 'g')
