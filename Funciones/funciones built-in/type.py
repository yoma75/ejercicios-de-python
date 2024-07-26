# type: retorna el tipo del objeto especificado

def tipoDato(valor):
    return type(valor)

print(tipoDato(True))                             # <class 'bool'>
print(tipoDato(45))                               # <class 'int'>
print(tipoDato(98.5))                             # <class 'float'>
print(tipoDato('Hola Python!'))                   # <class 'str'>
print(tipoDato(['a', 'e', 'i', 'o', 'u']))        # <class 'list'>
print(tipoDato(('a', 'e', 'i', 'o', 'u')))        # <class 'tuple'>
print(tipoDato({'animal':'salvaje', 'edad': 3}))  # <class 'dict'>

print(tipoDato(1j))                      # <class 'complex'>
print(tipoDato(range(6)))                # <class 'range'>
print(tipoDato(b"Hola"))                 # <class 'bytes'>
print(tipoDato(bytearray(5)))            # <class 'bytearray'>
print(tipoDato(memoryview(bytes(5))))    # <class 'memoryview'>
print(tipoDato(None))                    # <class 'NoneType'>
print(tipoDato(frozenset({"apple", "banana", "cherry"})))  # <class 'frozenset'>
