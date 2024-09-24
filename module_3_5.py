def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    while len(str_number) > 1:
        if int(str_number[1:]) == 0:
            return first
        else:
            first = first * get_multiplied_digits(int(str_number[1:]))
            print('2) first', first, 'number', number)
        return first
    else:
        return first

result = get_multiplied_digits(40203)
print(result)


