# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

# def user_info(name, age, city):
#     print('{}, {} год(а), проживает в городе {}.'.format(name, age, city))
#
# # user_info('Александр', 28, 'Челябинск')
# name = (input('Введите имя: ')).title()
# age = int(input('Введите возраст: '))
# city = input('Введите город: ')
# user_info(name, age, city)


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
def max_num(nums):
    return max(nums)

print('Bведите три числа.')
nums = []
while len(nums)<3:
    num = int(input('Введите число: '))
    nums.append(num)

result = max_num(nums)
print('Maximum number is ', result)

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов