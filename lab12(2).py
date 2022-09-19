a = int(input('Введите сумму к оплате: '))
b = int(input('Введите текущий час: '))
if  10 >= b <= 12:
    c = a/2
    print('К оплате:',c)
else:
    if 20 <= b <= 22:
        c = a/4
        print ('К оплате:', c)
    else:
        if 8 <= b <= 9:
             print('К оплате:', a)
        else:
            if 13 <= b <= 19:
                print('К оплате:', a)

