def calcular_hora_siguiente(hora, minuto, segundo):
    # Verificar si el segundo es menor a 59
    if segundo < 59:
        segundo_siguiente = segundo + 1
        minuto_siguiente = minuto
        hora_siguiente = hora
    else:
        # Si el segundo es 59, reiniciamos a 0 y aumentamos el minuto
        segundo_siguiente = 0

        # Verificar si el minuto es menor a 59
        if minuto < 59:
            minuto_siguiente = minuto + 1
            hora_siguiente = hora
        else:
            # Si el minuto es 59, reiniciamos a 0 y aumentamos la hora
            minuto_siguiente = 0

            # Verificar si la hora es menor a 23
            if hora < 23:
                hora_siguiente = hora + 1
            else:
                # Si la hora es 23, reiniciamos a 0, ya que el día tiene 24 horas
                hora_siguiente = 0

    return hora_siguiente, minuto_siguiente, segundo_siguiente

try:
    hora_actual = int(input("Introduce la hora (0-23): "))
    minuto_actual = int(input("Introduce el minuto (0-59): "))
    segundo_actual = int(input("Introduce el segundo (0-59): "))

    nueva_hora, nuevo_minuto, nuevo_segundo = calcular_hora_siguiente(hora_actual, minuto_actual, segundo_actual)

    print(f"La hora siguiente será: {nueva_hora:02d}:{nuevo_minuto:02d}:{nuevo_segundo:02d}")

except ValueError:
    print("Error: Asegúrate de ingresar valores numéricos válidos para la hora, minuto y segundo.")


'''explicacion del código anterior paso a paso:

1. Definición de la función `calcular_hora_siguiente(hora, minuto, segundo)`: Esta función toma tres argumentos: `hora`, `minuto` y `segundo`, que representan la hora actual en el formato H:M:S. La función se encargará de calcular la hora que será un segundo después de la hora actual.

2. Verificación del segundo: Primero, la función verifica si el segundo actual (`segundo`) es menor que 59. Si es así, significa que podemos simplemente incrementar el segundo en 1 para obtener el segundo siguiente (`segundo_siguiente`). Los minutos y horas permanecen sin cambios.

3. Segundos, minutos y horas próximos: Si el segundo actual es 59, eso significa que cuando agreguemos 1 segundo, el segundo siguiente será 0. En ese caso, debemos verificar también el minuto.

4. Verificación del minuto: Si el minuto actual (`minuto`) es menor que 59, podemos simplemente incrementar el minuto en 1 para obtener el minuto siguiente (`minuto_siguiente`). La hora permanece sin cambios.

5. Minutos y horas próximos: Si el minuto actual es 59, eso significa que cuando agreguemos 1 minuto, el minuto siguiente será 0. En este punto, debemos verificar también la hora.

6. Verificación de la hora: Si la hora actual (`hora`) es menor que 23, podemos simplemente incrementar la hora en 1 para obtener la hora siguiente (`hora_siguiente`).

7. Hora siguiente al final del día: Si la hora actual es 23, eso significa que cuando agreguemos 1 hora, la hora siguiente será 0, ya que un día tiene 24 horas.

8. Retorno de resultados: Finalmente, la función retorna los valores de la hora, minuto y segundo siguientes como una tupla `(hora_siguiente, minuto_siguiente, segundo_siguiente)`.

9. Entrada del usuario: El programa solicita al usuario que ingrese la hora, minuto y segundo actuales por separado y los convierte a números enteros.

10. Cálculo y visualización de la hora siguiente: Luego, llama a la función `calcular_hora_siguiente` con los valores ingresados por el usuario y muestra el resultado de la hora siguiente en el formato H:M:S.

Espero que esta explicación te ayude a entender cómo funciona el código. Si tienes alguna otra pregunta o necesitas más aclaraciones, no dudes en preguntar.'''
