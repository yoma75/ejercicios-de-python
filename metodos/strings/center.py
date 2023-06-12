# center(): permite centrar una frase o palabra segun los espacios dados

texto = ' Este es un titulo '
print('----------------------------'.center(129))
print(texto.center(130))
print('----------------------------'.center(129))

# ----------------------------
#      Este es un titulo
# ----------------------------

# Usando el caracter * para rellenar
print(texto.center(45, '*'))  # ************** Este es un titulo **************
