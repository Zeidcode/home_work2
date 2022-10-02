""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """


def input_nums(input_txt):
    is_OK = False
    while not is_OK:
        try:
            num = int(input(f"{input_txt}"))
            is_OK = True
        except ValueError:
            print("Число должно быть типа int ")
    return num


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = input_nums("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")