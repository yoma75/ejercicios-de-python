import numpy as np

array1 = np.arange(6)
print(array1)  # [0 1 2 3 4 5]

# Los archivos: guardar.npy y guardar2.npz, quedan salvados dentro en la carpeta principal

# Guardar 1 array, nombre_archivo.npy
np.save('guardar.npy', array1)  
np.load('guardar.npy')  # recargar el array guardad0
print(array1)

array2 = np.arange(9)
print(array2)


# Guardar 2 arrays en la variable guardar2
np.savez('guardar2', x=array1,y=array2)
array_recuperado = np.load('guardar2.npz')
print(array_recuperado['x'])
print(array_recuperado['y'])



