# Напишите класс-итератор, объекты которого генерируют случайные числа
# в количестве и в диапазоне, которые передаются в конструктор.

from random import randrange


class Digit:
    def __init__(self, digit):
        self.digit = []
        self.quantity = 10
        self.first = 1
        self.last = 100000
        for _ in range(digit):
            self.digit.append(str(randrange(self.first, self.last + 1)))

    def __iter__(self):
        return DigitIterator(self.digit[:])


class DigitIterator:
    def __init__(self, digit):
        self.digit = digit

    def __iter__(self):
        return self

    def __next__(self):
        if self.digit == []:
            raise StopIteration
        item = self.digit[0]
        del self.digit[0]
        return item

kit = Digit(10)
print(kit.digit)
for i in kit.digit:
    print(i)

# В задании к прошлому уроку требовалось написать класс-итератор, объекты которого генерируют случайные числа
# в количестве и в диапазоне, которые передаются в конструктор. Напишите выполняющую ту же задачу генераторную
# функцию. В качестве аргументов она должна принимать количество элементов и диапазон.

digitList = (randrange(0, 100000) for _ in range(10))
print(digitList)
