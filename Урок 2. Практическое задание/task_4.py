"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
def sum_arr(arr, size):
    if (size == 0):
        return 0
    else:
        return arr[size - 1] + sum_arr(arr, size - 1)
n = int(input("Введите длину ряда чисел для вычисления : "))
a = []
for i in range(0, n):
    element = float(input("Введите любое число ( вместо знака ',' используется '.' : "))
    a.append(element)
print("Все введенные числа : ")
print(a)
print("Сумма всех введенных чисел равна : ")
b = sum_arr(a, n)
print(b)

