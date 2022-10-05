# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний 
# и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]
res_lst = []

if len(lst) % 2 == 0:
    for i in range(len(lst)/2):
        result = lst[i] * lst[-i-1]
        res_lst.append(result)
    print(res_lst)
else:
    for i in range((len(lst)+ 1)//2):
        result = lst[i] * lst[-i-1]
        res_lst.append(result)
    print(res_lst)