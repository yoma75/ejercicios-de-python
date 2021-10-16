# copy: devuelva una copia de un conjunto, ya que éstos como la mayoría de colecciones se almacenan por referencia:

c = {21, 86, 93, 65}
c1 = {1, 2, 3, 4}
c2 = c.copy()

print(c1, c2)  # {1, 2, 3, 4} {65, 93, 21, 86}

c2.discard(86)
print(c1, c2)  # {1, 2, 3, 4} {65, 93, 21}
