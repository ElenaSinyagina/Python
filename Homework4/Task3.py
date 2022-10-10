# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

lst = [1, 2, 1, 3, 2, 4, 5]
rep_lst = []
result = []
for i in range (1,len (lst)):
    if lst.count(i)>1:
        rep_lst.append(i)

result = set(lst) - set(rep_lst)
print(lst)
print(list(result))