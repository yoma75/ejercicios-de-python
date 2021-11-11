# issubset: retorna verdadero si todos los items de un conjunto estan presentes en el otro

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
print(z)  # True por a, b, c


# ----------- ejemplo 2 --------------
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}

h = x.issubset(y)
print(h)  # False
