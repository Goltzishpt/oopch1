# Разработайте программу по следующему описанию.
# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде. 
# У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно. 
# Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде с более длинным списком, увеличивается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.


from random import randint, choice


class Person:
    def __init__(self):
        self.id = randint(0, 100)  # неуникальный номер объекта

    def info(self):
        infoList = [str(self.id)]  # сранный айдишник в виде листа переведенный в строку чтобы не было буилтинчетотам
        return ''.join(infoList)


class Heroes(Person):
    def __init__(self):
        super(Heroes, self).__init__()
        self.level = 1


def selectTeam(self, team='pink'):  # выбор команды героя
        select = input('Choose your team(0/1):')
        if select == 1:
            team = 'violet'
        return team

    def levelUp(self, teamSolid):
        if self.teamSolid == 'pink':
            self.level += 1
        print(f'Герой {Heroes.info(self)} команда достиг уровня {self.level}')


class Soldier(Person):
    def __init__(self, pinkTeam=[], violetTeam=[]):
        super(Soldier, self).__init__()
        self.teamSold = choice(['pink', 'violet'])
        if self.teamSold == 'pink':
            pinkTeam.append(0)
        else:
            violetTeam.append(0)

    def goToHero(self, Heroes):
        print(f'Солдат № {Soldier.info(self)} из команды {self.teamSold} следует за героем № {Heroes.info()}.')


hero1 = Heroes()
hero2 = Heroes()

soldiers = []
for i in range(10):
    soldiers.append(Soldier())

for j in soldiers:
    j.goToHero(choice([hero1, hero2]))
