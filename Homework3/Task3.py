# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


lst = [1.1, 1.2, 3.1, 5, 10.01]
new_lst = []

for i in range(len(lst)):
    result = round((lst[i] % 1), 2)
    if result != 0:
        new_lst.append(result)
print(new_lst)
print(max(new_lst))
print(min(new_lst))
print(round((max(new_lst) - min(new_lst)), 2))
