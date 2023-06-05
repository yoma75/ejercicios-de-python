# Muestra el nombre del sistema operativo y la version de la plataforma

import platform 
import os

print(os.name) # nt
print(platform.system()) # windows

# version de la plataforma
print(platform.release()) # 10

