# Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

n = int(input('Введите число N: '))
product = list(map(lambda x: math.factorial(x), range(1, n + 1)))
print(product)

exit()

# изначальный код

n=int(input('Введите число N: '))
product = 1
for i in range(1,n+1):
    product *= i
    print(product, end=' ')