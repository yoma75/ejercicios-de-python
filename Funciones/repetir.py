# escriba una línea formada por 2 letras, repetidas varias veces. Por ejemplo, para "-", "=" y 3, escribiría "-=-=-=".

def repetir(letra1, letra2, veces):
  for x in range(0, veces):
    print (letra1, end='')
    print (letra2, end='')

repetir("-", "=", 3)  # -=-=-=
repetir("/", "*", 5)  # /*/*/*/*/*
repetir("$", "+", 10) # $+$+$+$+$+$+$+$+$+$+
