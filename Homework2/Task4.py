#  Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


n=int(input('Введите число: '))
some_list = []
result = 1

for i in range (n):
    some_list.append(randint(-n, n))

file = open('file.txt', 'r')

for line in file:
    result *= some_list[int(line)]
    
file.close()

print(some_list)
print(result)