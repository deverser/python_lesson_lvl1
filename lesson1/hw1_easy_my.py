# -*- coding: utf-8 -*-
# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран
a = 1
b = 'hello world!'
c = 2.3

print('a =', a)
print('b =', b)
print('c =', c)
word = input('Введите слово  ')
print('Вы ввели', word)
print('Вы восхитительны!')

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

num = int(input('Введите число\n '))
print('Вы ввели ', num)
# num +=2
print("Мы прибавили к числу 2 и получили: ", num + 2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Введите ваш возраст: \n '))
if age >= 18:
    print('Доступ разрешен')
else:
    print("Извините, пользование данным ресурсом только с 18 лет")