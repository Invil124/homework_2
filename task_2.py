
## Вибачте що намудрив), провіряв можилвості map і трохи увлікся перевірками

ITER = 0

def check_integer(integer):
    if not integer:
        return False
    elif not integer.isdigit():
        global ITER
        ITER += 1
        print(f'{ITER} value is not an integer')
        return False
    else:
        return int(integer)

def input_two_integers():
     list_integers = input("Enter two numbers: ").strip().split(" ")
     if len(list_integers) != 2:
         print('You should input two digits with space')
         return [False,False]
     else:
         return list_integers

while True:
    a, b = map(check_integer, input_two_integers())
    ITER = 0

    if a is False or b is False:
        continue
    if a == b:
        print(f'Numbers are equal {a}={b}')
        break
    else:
        list_a_b = [a,b]
        print(f'{max(list_a_b)} > {min(list_a_b)}')
        break