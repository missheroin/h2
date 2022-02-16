def stroka(sp, rvn, simb, num):
    stroka = ''
    for i in sp:
        a = ''
        r = ''
        if rvn == 'center':
                r = '^'
        elif rvn == 'left':
                r = '<'
        elif rvn == 'right':
                r = '>'
        a = ('{0:%s%s%d}'%(simb, r, num)).format(i)
        stroka = stroka + '\n' + a
        a = ''
    return stroka[1::]

print(stroka([1, 2, 3, 4], 'center', '*', 9))
