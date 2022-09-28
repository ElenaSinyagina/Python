# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


ax=float(input ('Введите координату Х для точки А: '))
ay=float(input ('Введите координату Y для точки А: '))
bx=float(input ('Введите координату Х для точки В: '))
by=float(input ('Введите координату Y для точки В: '))
result=round(math.sqrt((bx-ax)**2 + (by-ay)**2), 2)
print('Расстояние между точками: ', result)