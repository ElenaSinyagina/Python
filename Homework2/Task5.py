# Реализуйте алгоритм перемешивания списка.

import random

some_list = []
for i in range (10):
    some_list.append(i)
print(some_list)
random.shuffle(some_list)
print(some_list)