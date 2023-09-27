a = int(input('Введите число от 28 до 30:'))
if a > 28 and a < 30:
    print('попал')
elif a >= 30:
    print('перелет')
elif a > 0 and a <= 28:
    print('недолет')
else:
    print('не бей по своим')

