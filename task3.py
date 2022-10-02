""" Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число."""

from random import randint


def input_nums(input_txt):
    is_OK = False
    while not is_OK:
        try:
            num = int(input(f"{input_txt}"))
            is_OK = True
        except ValueError:
            print("Какое-то неправильное число!")
    return num


def fill_list(diap):
    target_list = []
    for i in range(diap):
        target_list.append(randint(-diap, diap))
    return target_list


def check_list(num, diap, target_list):
    if -diap < num < diap:
        for i in target_list:
            if i == num:
                print("Yes")
                break
        else:
            print("No")
    else:
        print("число вне пределов ")


diapazon = input_nums("Введите диапазон (от -х до +х) и он же размер списка: ")

target_list = fill_list(diapazon)

print(target_list)

check_num = input_nums("Введите проверяемое число: ")

check_list(check_num, diapazon + 1, target_list)