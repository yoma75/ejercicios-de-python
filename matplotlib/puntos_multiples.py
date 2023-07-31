# Puntos múltiples
# Puedes trazar tantos puntos como quieras, solo asegúrate de tener el mismo número de puntos en ambos ejes.

# Dibuja una línea en un diagrama desde la posición (1, 3) a (2, 8) luego a (6, 1) y finalmente a la posición (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
