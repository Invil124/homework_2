

while True:
    integer = input('Input integer:').strip()
    if integer.isdigit():
        integer = int(integer)
        if integer % 3 == 0 and integer % 5 ==0:
            print('ham')
        elif integer % 3 == 0:
            print('foo')
        elif integer % 5 == 0:
            print('bar')
        else:
            print('not dividing on 3 or 5 ')
    else:
        print('IT NOT AN INTEGER')