# COMPARACIONES DE CONJUNTOS:

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

# isdisjoint: comprueba si el conjunto es disyunto de otro conjunto, es decir, si no hay ningún elemento en común entre ellos:
print(c1.isdisjoint(c2))  # False


# issubset: comprueba si el conjunto es subconjunto de otro conjunto, es decir, si sus ítems se encuentran todos dentro de otro:
print(c3.issubset(c4))  # False


# issuperset: comprueba si el conjunto es contenedor de otro subconjunto, es decir, si contiene todos los ítems de otro:
c3.issuperset(c1)  # False


# MÉTODOS AVANZADOS:
# Se utilizan para realizar uniones, diferencias y otras operaciones avanzadas entre conjuntos.

# Suelen tener dos formas, la normal que devuelve el resultado, y otra que hace lo mismo pero actualiza el propio resultado.

# union: une un conjunto a otro y devuelve el resultado en un nuevo conjunto:
c1 = {1,2,3}
c2 = {3,4,5}
c3 = c1.union(c2)
print(c1, "+", c2, "=", c3)  # {1, 2, 3} + {3, 4, 5} = {1, 2, 3, 4, 5}


# update: une un conjunto a otro en el propio conjunto:
c1.update(c2)
print(c1)  # {1, 2, 3, 4, 5}


# difference: encuentra los elementos no comunes entre dos conjuntos:
c1 = {1,2,3}
c2 = {3,4,5}
print(c1.difference(c2))  # {1, 2}


# difference_update: guarda en el conjunto los elementos no comunes entre dos conjuntos:
c1.difference_update(c2)
print(c1)  # {1, 2}


# intersection: devuelve un conjunto con los elementos comunes en dos conjuntos:
c1 = {1,2,3}
c2 = {3,4,5}
print(c1.intersection(c2))  # {3}


# intersection_update: guarda en el conjunto los elementos comunes entre dos conjuntos:
c1.intersection_update(c2)
print(c1)  # {3}


# symmetric_difference: devuelve los elementos simétricamente diferentes entre dos conjuntos, es decir, todos los elementos que no concuerdan entre los dos conjuntos:
c1 = {1,2,3}
c2 = {3,4,5}
print(c1.symmetric_difference(c2))  # {1, 2, 4, 5}
