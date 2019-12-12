'''
Составить алгоритм: на входе есть числовой массив,
необходимо вывести элементы массива кратные 3
'''

import random

my_list = [random.randint(1, 100) for i in range(20)]


def array_multiplicity(lst):
    for item in lst:
        if item % 3 == 0:
            print(item)


array_multiplicity(my_list)
