# Escribe un programa que tome una lista y elimine todos los elementos duplicados, dejando solo una instancia de cada elemento en la lista resultante

def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

mi_lista = [1, 2, 3, 4, 1, 2, 5, 3, 6, 4]
lista_sin_duplicados = eliminar_duplicados(mi_lista)

print(f'Lista original: {mi_lista}')
print(f'Lista sin duplicados: {lista_sin_duplicados}')  # [1, 2, 3, 4, 5, 6]


'''En este programa, se define una función llamada eliminar_duplicados que toma una lista como parámetro. Dentro de la función, se convierte la lista en un conjunto (set) utilizando set(lista). Un conjunto NO permite elementos duplicados, por lo que se eliminan automáticamente los duplicados. Luego, se convierte nuevamente el conjunto en una lista utilizando list(set(lista)) y se asigna a la variable lista_sin_duplicados.'''
