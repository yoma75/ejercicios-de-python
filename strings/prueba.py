def run():
    nombre_lista = []
    frase = input('Escribe la frase: ')
    nombre_lista.append(frase)    

    for x in nombre_lista:
        print(x.replace(' ', '\n'))


if __name__ == "__main__":
    run()

