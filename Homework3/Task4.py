# 4. Напишите программу, которая будет преобразовывать десятичное 
# число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
bin_num = []

bin_num.append(str(0 if number%2 == 0 else 1))
while number > 1:
    number = number // 2
    bin_num.append(str(0 if number%2 == 0 else 1))
bin_num.reverse()
print(''.join(bin_num))
