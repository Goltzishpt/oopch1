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
        if digit == []:
            raise StopIteration
        item = digit[0]
        del digit[0]
        return item

kit = Digit(10)
print(kit.digit)
for i in kit.digit:
    print(i)

