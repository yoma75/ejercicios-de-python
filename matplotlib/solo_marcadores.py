# Para trazar solo los marcadores, puede usar el parámetro de notación de cadena de acceso directo 'o', que significa 'anillos'.

# Dibuja dos puntos en el diagrama, uno en la posición (1, 3) y otro en la posición (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
