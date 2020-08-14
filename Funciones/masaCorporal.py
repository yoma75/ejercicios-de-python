# Calcular el Índice de Masa Corporal (IMC)

def imc(estatura, peso):
    return peso / estatura**2

peso = float(input('Escribe tu peso corporal: '))
estatura = float(input('Escribe tu estatura: '))

indice = imc(estatura,peso)

print()
print('Su Indice de Masa Corporal (IMC) es: {r:2.3}'.format(r=indice))

if indice < 18.5:
    print('Estas bajo de peso')
elif indice >= 18.5 and indice < 24.9:
    print('Peso normal')
elif indice >= 25 and indice <= 29.9:
    print('Sobrepeso')
elif indice >= 30 and indice < 34.9:
    print('obesidad')
else:
    print('Estas muy gordooooo para tu estatura')

