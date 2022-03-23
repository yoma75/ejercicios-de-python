# Encontrar la ruta de los site-packages de la instancia de python
# site-packages: los módulos que trae por defecto python 
# getsitepackages: Devuelve una lista que contiene todos los directorios globales de paquetes de sitio.


import site

print(site.getsitepackages())


