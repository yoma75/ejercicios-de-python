# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de libras y muestre por pantalla el precio de ese número de libras de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	    Precio
# Plátano	 1.350
# Manzana	 800
# Pera	     850
# Naranja	 700

# Crear diccionario:
# llaves : valor

def run():
    frutas = {'platano':1350, 'manzana':800, 'pera':850, 'naranja':700}

    frutica = input('\nQue fruta desea: '.upper())
    libras = float(input('Cuantas libras: '))

    if frutica in frutas:
        print(f'{libras} libras de {frutica} cuestan: {round(frutas[frutica]*libras)} pesos')
    else:
        print(f'Lo siento la fruta {frutica} esta agotada')


if __name__ == "__main__":
    run()

