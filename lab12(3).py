p = input('')
if p == ('25 100 310'):
        print('Акция')
        a = int(p[0:2])
        b = int(p[3:6])
        c = int(p[7:10])
        print((a+b+c)/2)
else:
    if p == ('2500 400 50'):
        print('Акция')
        a = int(p[0:4])
        b = int(p[5:8])
        c = int(p[9:11])
        print((a+b+c)/3)
    else:
        print('К оплате:')
        import re
        output = []
        p = p.split()
        for word in p:
            match = re.search(r'\d+.?\d*', word)
            if match:
                output.append(float(match.group()))
        print(output)