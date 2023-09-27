qwe = int(input('введите год: '))
if qwe % 4 == 0:
    if qwe % 100!= 0:
        print('да')
    else:
        if qwe % 400 == 0:
            print('да')
        else:
            print('нет')
else:
    print('нет')
