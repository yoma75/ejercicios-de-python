# isdisjoint: retorna verdadero (True) si los items de un conjunto NO estan presentes en el otro conjunto

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)
print(z)  # True