# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def filter (text):
    list = text.split (' + ')
    for i in range (len (list)):
        text = list [i]
        if '0' <= text [0] <= '9':
            char = text [0]
            if len (text) > 1:
                j = 1 
                while '0' <= text [j] <= '9':
                    char += text [j]
                    j += 1            
            list [i] = char
        else: list [i] = 0   
    return list

with open('file1.txt') as file:
    first = str (file.readline())

with open('file2.txt') as file:
    second = str (file.readline())

first = filter (first)
second = filter (second)
result = []
for i in range (len (first)):
    result.append(int(first [i]) + int(second[i]))


data = open ('result.txt','a')
for i in range (len(first)-1):    
    data.write (str(result[i]) + '*x^' + str (len(first) - i - 1) + ' + ')
data.write (str(result[len(first)-1]))
data.write('\n')
data.close()