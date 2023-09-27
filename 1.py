a = int(input('Ведите первое число '))
b = int(input('Ведите второе число '))
c = int(input('Ведите третье число '))
if a>b and a>c:
    print(f'Максимально число {a}')
elif b>a and b>c:
    print(f'Максимально число {b}')
else:
    print(f'Максимально число {c}')

