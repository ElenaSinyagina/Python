# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint

k = int(input('Введите степень k > 0: '))
if k <= 0:
    print("Вы ввели значение k меньше или равное 1")
def func(k):
    data = open("file.txt", "a")
    a=int(0)
    for i in range(-k, -1):
        a=randint(0, 101)
        if a != 0:
            data.write (str(a))
            data.write ('*x^')
            data.write (str(-i))
            data.write ('+')
    a=randint(0, 101)
    if a != 0:
        data.write (str (a))
        data.write ('*x+')
    a=randint(0, 101)
    if a != 0:
        data.write (str (a))
        data.write ('=0')
        data.write('\n')        
    data.close()

func(k)

