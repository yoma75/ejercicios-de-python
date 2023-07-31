# Dibuja una línea en un diagrama desde la posición (0,0) hasta la posición (6.250):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()


'''
plot(ejeX, ejeY): esta función se utiliza para dibujar puntos (marcadores) en un diagrama, dibuja una línea de punto a punto.

La función toma parámetros para especificar puntos en el diagrama.
El parámetro 1 es una matriz que contiene los puntos del eje x.
El parámetro 2 es una matriz que contiene los puntos del eje y.

Si necesitamos trazar una línea de (1, 3) a (8, 10), tenemos que pasar dos matrices [1, 8] y [3, 10] a la función de trazado.
'''
