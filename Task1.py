# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def sum(num: str):
    sum_ = 0
    for i in range(len(num)):
        if num[i].isdigit():
            sum_ += int(num[i])
    return sum_

a = input('Введите число: ')
print(sum(a))