# Calcular la estatura de una persona en pulgadas y pies
# 1 ft (pie): equivale a 30.48 cm
# 1 pulgada: 2.54 cm

estatura = float(input('Cual es tu estatura en cms: '))

pie = estatura / 30.48
pulgada = estatura / 2.54

print(f'La conversion de tu estatura de centimetros a pies es: {pie}')
print('La conversion de tu estatura de centimetros a pulgadas es: {r:1.2}'.format(r=pulgada))



