class Person:
    sex = str()

    def __init__(self, name, surname, quality=1, sex='female'):
        self.name = name
        self.surname = surname
        self.quality = quality
        self.sex = sex

    def ret(self):
        who = [self.name, self.surname]
        return ' '.join(who)

    def __del__(self):
        who = [self.name, self.surname]
        if self.sex == 'male':
            iden = 'Mr'
        else:
            iden = 'Mrs'
        print(f'Goodbye, {iden} {" ".join(who)}')


p1 = Person('Vi', 'Goltz', 3)
p2 = Person('Irma', 'Homenko', 4)
p3 = Person('Vlad', 'Dolotov', 2, 'male')

print(p1.ret())
print(p2.ret())
print(p3.ret())
del(p3)


input()
