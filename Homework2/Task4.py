#  Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n=int(input('Введите число: '))
some_list = []
for i in range (-n, n+1):
    some_list.append(i)
with open('file.txt') as file:
    a = int(file.readline())
    b = int(file.readline())
print(some_list)
result = some_list[a] * some_list[b]
print(result)