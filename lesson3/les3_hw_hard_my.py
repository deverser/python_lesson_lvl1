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

hero = {'name': None, 'health': 100, 'damage': 50, 'armor':1.2}
enemy = {'name': None, 'health': 250, 'damage': 32, 'armor':1.5}

def give_name(person, name=None):
    '''Даем имена героям игры и записываем их в словари'''
    name = input('Введите имя игрока: ')
    person['name'] = name.title()
    return person


def save_params(**person):
    '''Сохранение параметров персонажей в файлы'''
    filename = person['name'] + '.txt'
    with open(filename, 'w', encoding="utf-8") as file:
        for key, value in person.items():
            file.write('{} - {}\n'.format(key, value))
            
def read_params(**person):
    param_dict = {}
    filename = person['name'] + '.txt'
    with open(filename, 'r', encoding = 'utf-8') as file:
        for line in file:
            tmp = line.split(' - ')
            param_dict[tmp[0]] = tmp[1]
    return param_dict
    
    
def damage_get(damage, armor=1.2):
    '''Вычисление полученного урона с учётом брони'''
    dmg_get = round(damage/armor, 1)
    return dmg_get

def attack(player1, player2):
    '''Атаки персонажей'''
    fight = []                # создаем словарь, в который будем писать атаки персонажа 
    name1 = player1['name']
    name2 = player2['name']
    damage = damage_get(player1['damage'],player2['armor'])
    health = player2['health']
    health1 = player1['health']
    armor = player1['armor']
    print('{} has {} xp and {} armor'.format(name1, health1, armor)) 
    while health > 0:
        health = round((health - damage),1)      # пока здоровье одного из героев не упадет до нуля 
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

# сохраняем параметры героев в файлы
save_params(**hero)
save_params(**enemy)


print(read_params(**hero))
print(read_params(**enemy))

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
