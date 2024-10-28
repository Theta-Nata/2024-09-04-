total_sum = 0
def sum_all(*args):
    global total_sum
    for i in args:
        if isinstance(i, (int, float)):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                total_sum = sum_all(key, value)
        elif isinstance(i, (list, tuple,set)):
           total_sum = sum_all(*i)
    return total_sum


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

print('сумма всех чисел и длин всех строк =', sum_all(*data_structure))