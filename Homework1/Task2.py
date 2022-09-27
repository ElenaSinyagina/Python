# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x=int(input('Введите значение X: '))
y=int(input('Введите значение Y: '))
z=int(input('Введите значение Z: '))
if not (x or y or z) == (not x) and (not y) and (not z):
    print('True')
else:
    print('False')