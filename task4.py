# Задайте список из N элементов, заполненных  числами из промежутка [-N, N]. Найдите  произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input('Введите число: '))
num_list = []
for i in range(-num, num+1):
    num_list.append(i)

print(num_list)

result = 1

data = open('file.txt', 'r')
temp_list = data.readlines()
print(temp_list)

for line in data:
    temp =int(line)
    print(temp)
    result *= num_list[temp]
data.close()    
print(result)    