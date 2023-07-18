# Calcular los multiplos de 4 comprendidos entre 4 y N, donde N es un valor introducido por teclado:

def calcular_multiplos_de_cuatro(N):
    multiplos_de_cuatro = []

    for num in range(4, N + 1):
        if num % 4 == 0:
            multiplos_de_cuatro.append(num)

    return multiplos_de_cuatro

if __name__ == "__main__":
    try:
        N = int(input("Introduce un valor entero N: "))
        if N >= 4:
            multiplos = calcular_multiplos_de_cuatro(N)
            print(f"Los múltiplos de 4 comprendidos entre 4 y {N} son: {multiplos}")
        else:
            print("El valor debe ser mayor o igual a 4.")
    except ValueError:
        print("Error: Debes introducir un número entero válido.")
