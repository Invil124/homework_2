

while True:
    integer = input('Input integer:').strip()
    if integer.isdigit():
        integer = int(integer)
        if integer % 3 == 0 and integer % 5 ==0:
            print('ham')
            break
        elif integer % 3 == 0:
            print('foo')
            break
        elif integer % 5 == 0:
            print('bar')
            break
        else:
            print('not dividing on 3 or 5 ')
    else:
        print('IT NOT AN INTEGER')