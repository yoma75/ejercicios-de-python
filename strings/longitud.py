# Cree una función que tome dos cadenas como argumentos y devuelva True o False dependiendo de si el número total de caracteres en la primera cadena es igual al número total de caracteres en la segunda cadena.

# Ejemplos
# comp("AB", "CD") ➞ True
# comp("ABC", "DE") ➞ False
# comp("hello", "edabit") ➞ False

def comp(txt1, txt2):
	if (len(txt1) == len(txt2)):
		return print(True)
	else:
		return print(False)

comp("AB", "CD")  # True
comp("ABC", "DE") # False
comp("hello", "edabit")  # False
