a = int(input(''))

if a > 0:
    b = a % 10
    c = b/2
elif a > 0:
    digit = a % 10
    a = a // 10
    print(a)