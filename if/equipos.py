# Partidos de fútbol, 6 equipos

# 1. America
# 2. Millonarios
# 3. Bucaros
# 4. Junior


# Listas para acumular los goles anotados
lista_america = []
lista_millos = []
lista_bucaros = []
lista_junior = []

suma_america, suma_millos = 0, 0
suma_bucaros, suma_junior = 0, 0

print()
print('------------------ Semi final -------------------------'.upper())
print('________ America Vs Millonarios __________'.upper())
america = int(input('America: '))
lista_america.append(america)
millos = int(input('Millonarios: '))
lista_millos.append(millos)
print()

if america == millos:
    print('Definición por penaltis')
    p_america = int(input('America: '))    
    lista_america.append(p_america)
    suma_america = (lista_america[0]+lista_america[1])

    p_millos = int(input('Millonarios: '))
    lista_millos.append(p_millos)
    suma_millos = (lista_millos[0]+lista_millos[1])

if suma_america > suma_millos:
    print(f'America gana con: {suma_america} goles en total')
else:
    print(f'Millonarios gana con: {suma_millos} goles en total')

# -----------------------------------------------------------------------------------
print()
print('________ Atlético Bucaramanga Vs Junior ________'.upper())
bucaros = int(input('Atletico Bucaramanga: '))
lista_bucaros.append(bucaros)
junior = int(input('Junior: '))
lista_junior.append(junior)
print()

if bucaros == junior:
    print('Definicion por penaltis')
    p_bucaros = int(input('Atletico Bucaramanga: '))    
    lista_bucaros.append(p_bucaros)
    suma_bucaros = (lista_bucaros[0]+lista_bucaros[1])

    p_junior = int(input('Junior: '))
    lista_junior.append(p_junior)
    suma_junior = (lista_junior[0]+lista_junior[1])

if suma_bucaros > suma_junior:
    print(f'Atletico Bucaramanga gana con: {suma_bucaros} goles en total')
else:
    print(f'Junior gana con: {suma_junior} goles en total')

# ---------------------------------------------------------------------------------
print()
print()
print('+++++++++++++ Equipos clasificados a la final +++++++++++++'.upper())
print()
if suma_america > suma_millos:
    print(f'- America: {lista_america}')
else:
    print(f'- Millonarios: {lista_millos}')

if suma_bucaros > suma_junior:
    print(f'- Atletico Bucaramanga: {lista_bucaros}')
else:
    print(f'- Junior ( Tu papa ) {lista_junior}')

# ------------------------------------------------------------------------------------
