def insta1(us):
    l = len(us)
    if l == 1:
        print('%s likes it'%(us[0]))
    elif l == 2:
        print('%s and %s likes it'%(us[0], us[1]))
    elif l == 3:
        print('%s, %s and %s likes it'%(us[0], us[1], us[2]))
    elif l > 3:
        print('%s and %d likes it'%(us[0], l - 1))

def insta2(us):
    l = len(us)
    if l == 1:
        print('{0:s} likes it'.format(us[0]))
    elif l == 2:
        print('{0:s} and {1:s} likes it'.format(us[0], us[1]))
    elif l == 3:
        print('{0:s}, {1:s} and {2:s} likes it'.format(us[0], us[1], us[2]))
    elif l > 3:
        print('{0:s} and {1:d} likes it'.format(us[0], l - 1))

def insta3(us):
    l = len(us)
    if l == 1:
        print(f'{us[0]} likes it')
    elif l == 2:
        print(f'{us[0]} and {us[1]} likes it')
    elif l == 3:
        print(f'{us[0]}, {us[1]} and {us[2]} likes it')
    elif l > 3:
        print(f'{us[0]} and {l - 1} likes it')

insta1(['aa', 'bb', 'cc', 'dd'])
insta2(['ee', 'ff', 'gg'])
insta3(['kk', 'll', 'mm'])