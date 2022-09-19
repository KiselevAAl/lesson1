u = int(input(''))
for i in range (u):
    name = input('Введите ваше музыкальное предпочтение:')
    print('Предпочтение учтено')
print('Система рекомендаций настроена!')



h = input('')
if h == ('Game'):
    print('Угадай число')
    a = int(input(''))
    while a < '5':
        print('Неправильный ответ')
        if a == 5:
            print('Неправильный ответ')
        else:
            print('Попробуй еще раз')
    print('Победа')




    username = input('Введите имя пользователя: ')
    username_correct = False

    while not username_correct:
        if username == '=, ?, *,^, $, №, @_':
            print('Пароль слишком короткий\n')
        elif username:
            print('Пароль содержит имя пользователя\n')
        else:
            print('Пароль для пользователя {} установлен'.format(username))
            password_correct = True
            continue
        password = input('Введите пароль еще раз: ')





