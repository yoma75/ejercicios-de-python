# format: 

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)


print(txt1)  # My name is John, I'm 36
print(txt2)  # My name is John, I'm 36
print(txt3)  # My name is John, I'm 36

# -------------------------------------------------------------------------------------------------------

texto = 'Tu porcentaje es del: {:%}'
print(texto.format(0.25))  # Tu porcentaje es del: 25.000000%


texto = 'Tu porcentaje es del: {:.0%}'
print(texto.format(0.89))  # Tu porcentaje es del: 89%


# inserta 8 espacios en caracteres en blanco
# ">" alinear a la derecha el valor
txt = "Nosotros tenemos {:>8} gatos."
print(txt.format(49))  # Nosotros tenemos       49 gatos.


# inserta 8 espacios en caracteres en blanco
# ">" alinear a la izquierda el valor
txt = "Nosotros tenemos {:<8} gatos."
print(txt.format(49))  # Nosotros tenemos 49      gatos.


# https://www.w3schools.com/python/ref_string_format.asp
