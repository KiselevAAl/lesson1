h = input('')
if h == ('Game'):
    print('Угадайте число')
    a = int(input('Ваше предположение: '))
    b = 2
while a != 5:
    if a > 5:
        print("Меньше...")
    else:
        print("Больше...")
    if b == 0:
        break
    a = int(input("Ваше предположение: "))
    b -= 1
if a != 5:
    print('Вы истратили все попытки, попробуйте еще раз')
else:
    print("Победа!")

