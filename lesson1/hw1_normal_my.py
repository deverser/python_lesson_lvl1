# -*- coding: utf-8 -*-
# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

num = -1
while True:
    num = int(input('Введите число:  \n'))
    if (0<num<10):
        print('Ваше число в квадрате будет: ', num**2)
        break
    else:
        print('Число неверное. Введите заново число от 0 до 10')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

num1 = int(input('Введите первую переменную: \n'))
num2 = int(input('Введите вторую переменную: \n '))