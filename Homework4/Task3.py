# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

list = [1, 2, 1, 3, 2, 4, 5]
rep_list = []
result = []
for i in range (1,len (list)):
    if list.count(i)>1:
        rep_list.append(i)

result = set(list) - set(rep_list)
print(result)