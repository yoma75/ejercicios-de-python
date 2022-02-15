from datetime import datetime

todayIs = datetime.now()

userYear = int(input('Digite su año de nacimiento: '.upper()))

print(f'Usted tiene: {(todayIs.year) - userYear} años\n')

