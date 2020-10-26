# Escribe una función que tome dos números enteros ( hours, minutes), los convierta en segundos y los sume.

def segundos(horas, minutos):    
    x = ((horas*60*60) + (minutos*60))
    return print(f'Total {x} segundos')

segundos(1,3)
segundos(2,0)
segundos(0,0)
