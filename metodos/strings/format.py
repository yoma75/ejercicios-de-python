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





