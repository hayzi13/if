a = int(input('Первая сторона  '))
b = int(input('вторая сторона  '))
c = int(input('третья сторона  '))
if a < b+c and b < a+c and c < a+b:
    print('да')
else:
    print('нет')
