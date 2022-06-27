'''Digite una extension y diga que clase de archivo es:'''

extension = {
    'pdf':'Documento Adobe PDF',
    'txt':'Documento de texto',
    'html':'pagina web',
    'ppt':'presentacion microsoft powerpoint',
    'doc':'documento microsoft word',
    'xls':'documento microsoft excel',
    'gif':'imagen gif',
    'jpg':'imagen jpg',
    'zip':'archivo comprimido'
}

x = input('\nDigite extension: ')

if x in extension:
    print(f'Significado: {extension[x]}\n')
else:
    print('No existe esa extensión')
