# Comprueba si el elemento buscado esta en la lista

def buscar(lista, elemento):
    for x in lista:
        if elemento == x:
            return True
    
    return False

print(buscar([2, 3, 5, 7, 11], 5)) # True
print(buscar([2, 3, 5, 7, 11], 19)) # False
print(buscar('Fork', 'k')) # True
print(buscar('Fork', 'i')) # False
