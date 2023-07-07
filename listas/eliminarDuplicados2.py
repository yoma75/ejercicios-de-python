#  Escribe un programa que tome una lista y elimine todos los elementos duplicados, dejando solo una instancia de cada elemento en la lista resultante

def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

mi_lista = [1, 2, 3, 4, 1, 2, 5, 3, 6, 4]
lista_sin_duplicados = eliminar_duplicados(mi_lista)

print(lista_sin_duplicados)  # [1, 2, 3, 4, 5, 6]


'''se define la función eliminar_duplicados que recibe una lista como parámetro. Dentro de la función, se inicializa una lista vacía llamada lista_sin_duplicados. Luego, se recorre cada elemento de la lista original utilizando un bucle for. Si el elemento no está presente en la lista lista_sin_duplicados, se agrega a esa lista utilizando append(). De esta manera, se garantiza que solo se agregue una instancia de cada elemento. Finalmente, se devuelve la lista sin duplicados.'''
