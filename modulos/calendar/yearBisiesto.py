import calendar

def yearBisiesto(year):
  return calendar.isleap(year)


print(yearBisiesto(1977))  # False
print(yearBisiesto(2000))  # True
print(yearBisiesto(2022))  # False