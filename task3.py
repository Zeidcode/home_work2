# Задайте список из n чисел последовательности по формуле (1+ 1 /n)**n и выведите на экран их сумму.Пример:- Для n = 6: [2, 2, 2, 2, 2, 3]   13
num = int(input('Введите число: '))
nums_list =[]
for i in range(1, num+1):
    temp = round( (1 + 1/i)**i )
    nums_list.append(temp)

print(nums_list)
sum = 0
for j in nums_list:
    sum +=j
print(sum)   