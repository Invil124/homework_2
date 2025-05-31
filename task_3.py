
i =0
list_numbers = []
while True:
    input_integer = input('Input integer: ').strip()
    if not input_integer.isdigit():
        print('Not a digit')
        continue
    else:
        list_numbers.append(int(input_integer))
        if len(list_numbers) == 3:
            max_integer = max(list_numbers)
            min_integer = min(list_numbers)
            median = sum(list_numbers) - max_integer - min_integer
            print(f'Max integer {max_integer}, min integer {min_integer}, median {median}')
            break
        else:
            i += 1
            print(i,'digit')
            continue