def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a = 1, b = 'строка', c = True)
print_params(a = 5, b = 3, c = 'строка')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [3, 2.2, 'python']
values_dict = {'a':7, 'b':True, 'c':'sign'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)