# Crea un programa con un bucle for y una declaración break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea:

for ch in "john.smith@pythoninstitute.org":
  if ch == "@":
    break
  print(ch, end="")  # john.smith
