#  Decir si es una letra o una vocal:

def es_vocal(x):
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        print(f'{x} es una vocal')
    else:
        print(f'{x} es una letra')

es_vocal('a')
es_vocal('h')
