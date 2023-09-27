a = int(input('Ведите первое число '))
b = int(input('Ведите второе число '))
c = int(input('Ведите третье число '))
if (a>b and a<c) or (a<b and a>c) :
    print(f'среднее число {a}')
elif (b>a and b<c) or (b<a and b>c) :
    print(f'среднее число {b}')
elif (c>a and c<b) or (c<a and c>b) :
    print(f'среднее число {c}')

else:
    print('ошибка')

