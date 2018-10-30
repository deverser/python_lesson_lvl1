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

hero = {'name': None, 'health': 100, 'damage': 45}
enemy = {'name': None, 'health': 200, 'damage': 15}

def give_name(person, name=None):
    '''Даем имена героям игры и записываем их в словари'''
    name = input('Введите имя игрока: ')
    person['name'] = name.title()
    return person


def attack(player1, player2):
    '''Битва персонажей'''
    fight = []
    name1 = player1['name']
    name2 = player2['name']
    damage = player1['damage']
    health = player2['health']
    while health > 0:
        health -= damage
        if health <=0:
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
    if len(attack1) > len(attack2):
##        delta = len(attack1) - len(attack2)
##        attack1 = attack1[:-delta]
        print(len(attack1))
        i = 0
        while i < len(attack2):
            print(attack1[i])
            print(attack2[i])
            i += 1
    else:
##        delta = len(attack2) - len(attack1)
##        attack2 = attack2[:-delta]
        print(len(attack2))
        i = 0
        while i < len(attack1):
            print(attack1[i])
            print(attack2[i])
            i += 1
        
    
give_name(hero)
give_name(enemy)

hero_attack = attack(hero,enemy)
enemy_attack = attack(enemy,hero)

print(len(hero_attack))
print(len(enemy_attack))

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
