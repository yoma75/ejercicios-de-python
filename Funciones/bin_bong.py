'''
Escribe una función llamada bing_bong que reciba un número como parámetro:

Si el número es múltiplo de 3 debe retornar "bing".
Si el número es múltiplo de 5 debe retornar "bong".
Si el número es múltiplo tanto de 3 como de 5 debe retornar "bingbong".
Si no cumple ninguna de las condiciones anteriores debe retornar el mismo número.
'''
  

def bing_bong(num):
  if ((num % 3 == 0) and (num % 5 == 0)):
    return 'bingbong'
  if (num % 3 == 0):
    return 'bing'
  elif (num % 5 == 0):
    return 'bong'  
  else:
    return num  


print(bing_bong(3))  # "bing"
print(bing_bong(5))  # "bong"
print(bing_bong(30)) # "bingbong"
print(bing_bong(8))  # 8