# chr: retorna la cadena que representa un carácter cuyo código Unicode es el entero. Por ejemplo, chr(97) retorna la cadena ’a’, mientras que chr(8364) retorna la cadena ’€’. Esta función es la inversa de ord().

def codigo(numero):
  return print(f'{chr(numero)}')

codigo(97)   # a
codigo(104)  # h
codigo(117)  # u


def inversa(numerito):
  return print(f'{ord(numerito)}')
  
inversa('a')  # 97
inversa('h')  # 104
inversa('u')  # 117
