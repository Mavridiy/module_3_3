# 1 задание
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1,2,3])


# 2 задание
def print_params(a, b, c):
    print(a, b, c)


values_list = [1, 'f', [3, 'word', True]]
values_dict = {'a': 4, 'b': False, 'c': 'line'}
print_params(*values_list)
print_params(**values_dict)


# 3 задание
def print_params(a, b, c):
    print(a, b, c)

values_list_2 = [values_list, True]
print_params(*values_list_2, 42)
