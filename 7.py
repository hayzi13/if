import math
print('1 - прямоугольник\n2 - треугольник\n3 - круг')
choice = int(input('? '))
if choice == 1:
    a = int(input('a: '))
    b = int(input('b: '))
    square = a*b
    print(square)
elif choice == 2:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    p = (a+b+c) / 2
    square = math.sqrt(p * (p-a)*(p-b)*(p-c))
    print(round(square, 2))
elif choice == 3:
    r = int(input('r: '))
    square = math.pi * r**2
    print(round(square, 2))
