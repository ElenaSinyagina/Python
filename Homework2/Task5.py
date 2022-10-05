# Реализуйте алгоритм перемешивания списка.

import random

some_list = []
for i in range (10):
    some_list.append(i)

print(some_list)

new_list = []
for j in range(len(some_list)):
    index = random.randint (0, len(some_list)-1)
    new_list.append(some_list[index])
    some_list.remove(some_list[index])
print(new_list)