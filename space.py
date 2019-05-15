def convert_this(a):
    options = ['p', 'k', 'm', 'g', 'q', 't']
    p = 0
    k = 0
    m = 0
    g = 0
    t = 0

    if len(a) == 0:
        a = ['p', p]
    elif len(a) == 1:
        a.append(0)

    a[0] = str(a[0])
    try:
        for i in range(len(a[1:])) :
            a[i + 1] = float(a[i + 1])
    except:
        return 'Use only numbers after first argument. First Argument in {}'.format(options)

    if a[0] not in options:
        return ('''Format your input:  Input_type num num num ...
Input_Types
-----------
p = pages
k = kilobytes
m = megabytes
g = gigabyte
t = Terabyte

q = quit
''')
    else:
        if a[0] == 'p':
            p = sum(a[1:])
            k = p * 8
            m = k / 1024
            g = m / 1024
            t = g / 1024
        elif a[0] == 'k':
            k = sum(a[1:])
            p = k / 8
            m = k / 1024
            g = m / 1024
            t = g / 1024
        elif a[0] == 'm':
            m = sum(a[1:])
            k = m * 1024
            p = k * 8
            g = m / 1024
            t = g / 1024
        elif a[0] == 'g':
            g = sum(a[1:])
            m = g * 1024
            t = g / 1024        
            k = m * 1024
            p = k / 8
        elif a[0] == 't':
            t = sum(a[1:])
            g = t * 1024
            m = g * 1024
            k = m * 1024
            p = k / 8
        elif a[0] == 'q':
            return False

            
            
        return '''pages = {}
KB = {}
MB = {}
GB = {}
TB = {}
'''.format(p, k, m, g, t)


if __name__ == '__main__':
    x = True
    while x == True:
        a = input('List of numbers to convert >> ').strip().lower().split()
        if convert_this(a) == False:
            x = False
            print('Exiting...')
        else:
            print(convert_this(a))




