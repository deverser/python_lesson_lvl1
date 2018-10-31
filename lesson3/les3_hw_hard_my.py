# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

hero = {'name': None, 'health': 100, 'damage': 25}
enemy = {'name': None, 'health': 200, 'damage': 43}

def give_name(person, name=None):
    '''Даем имена героям игры и записываем их в словари'''
    name = input('Введите имя игрока: ')
    person['name'] = name.title()
    return person


def attack(player1, player2):
    '''Атаки персонажей'''
    fight = []                # создаем словарь, в который будем писать атаки персонажа 
    name1 = player1['name']
    name2 = player2['name']
    damage = player1['damage']
    health = player2['health']
    while health > 0:
        health -= damage      # пока здоровье одного из героев не упадет до нуля 
        if health <=0:        # записываем атаки и добавляем их в список fight
            health = 0
            msg = '{} attacks {} with {}. {}\'s xp is {}. {} wins the fight!'.format(
                    name1, name2, damage, name2, health, name1)
            fight.append(msg)
            break
            return fight
        msg = '{} attacks {} with {} dmg. {}\'s xp is {}'.format(
            name1, name2, damage, name2, health)
        fight.append(msg)
    return fight

def battle(attack1,attack2):
    '''Битва персонажей'''
    if len(attack1) > len(attack2):
        i = 0               # объявляем переменную i для счетчика атак персонажа
        hits = len(attack2) # количество атак более мощного персонажа
        while i < hits:
            print(attack2[i]) # выводим сообщения об атаках мощного персонажа
            if i < hits - 1:  # так как 2й персонаж слабее, он сделает на один удар меньше чем 1й,
                print(attack1[i]) # поэтому все последующие сообщения на экран не выводятся
            i += 1        
    else:
        i = 0
        hits = len(attack1)
        while i < hits:
            print(attack1[i])
            if i < hits - 1:
                print(attack2[i])
            i += 1
        
# даем имена героям игры    
give_name(hero)
give_name(enemy)

# записываем все их атаки друг против друга и сохраняем их в 2х списках
hero_attack = attack(hero,enemy)
enemy_attack = attack(enemy,hero)

# устраиваем битву поочередно выводя в консоль сообщения об атаках, до тех пор
# пока не объявится победитель битвы
battle(hero_attack, enemy_attack)



# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
## после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
