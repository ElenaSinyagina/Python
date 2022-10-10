# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)

import math


n = 10000000
d = float(input('Введите d: '))
a = round(-math.log(d,10))

def func(n):
    num_pi = 0
    for i in range(1,n,4):
            num_pi = num_pi + 4/i - 4/(i + 2)
    return print(round(num_pi,int(a)))
    
func(n)


