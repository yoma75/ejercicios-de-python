# Puntos X predeterminados
# Si no especificamos los puntos en el eje x, obtendrán los valores predeterminados 0, 1, 2, 3 (etc., dependiendo de la longitud de los puntos y.

# Trazar sin puntos x:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])
# xpoints          [0, 1, 2,  3, 4, 5]


plt.plot(ypoints)
plt.show()
