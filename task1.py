""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """


def input_nums(input_txt):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{input_txt}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def sum_nums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = input_nums("Введите число: ")

print(f"Сумма цифр = {sum_nums(num)}")