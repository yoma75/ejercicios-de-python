#  Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

table = [[":(", ":)", ":(", ":)"],
        [":)", ":(", ":)", ":)"],
        [":(", ":)", ":)", ":("],
        [":)", ":)", ":)", ":("]]


for row in table:
  print(" ".join(row))

print(table[0][0])  # ':('
print(table[0][3])  # ':)'
print(table[2][0])  # ':('