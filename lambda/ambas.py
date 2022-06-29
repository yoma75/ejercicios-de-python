def myfunc(n):
  return lambda a : a * n

doble = myfunc(2)  # n = 2
triple = myfunc(3)

print(doble(11))  # a = 22
print(triple(11))  # 33
