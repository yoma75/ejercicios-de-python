# Realizar la cuenta de los enteros comprendidos entre dos limites, minimo y maximo

def contar_enteros(minimo, maximo):
    if minimo > maximo:
        return "El límite mínimo debe ser menor o igual al límite máximo."
    
    numeros = []
    for i in range(minimo, maximo + 1):
        numeros.append(i)
    
    return numeros

limite_minimo = int(input("Ingrese el límite mínimo: "))  # 6
limite_maximo = int(input("Ingrese el límite máximo: "))  # 11

resultado = contar_enteros(limite_minimo, limite_maximo)

print(f'Enteros comprendidos entre {limite_minimo} y {limite_maximo}: ')  # Enteros comprendidos entre 6 y 11: 
print(resultado)  # [6, 7, 8, 9, 10, 11]
