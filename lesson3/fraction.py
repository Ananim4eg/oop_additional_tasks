"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""


class Fraction:
    numerator: int
    denominator: int

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"{self.__class__.__name__}({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if self.denominator != other.denominator:
            if max(self.denominator, other.denominator) % min(self.denominator, other.denominator) == 0:
                if self.denominator > other.denominator:
                    new_numerator = int(other.numerator * (self.denominator / other.denominator))

                    return f"{self.numerator + new_numerator}/{self.denominator}"
                else:
                    new_numerator = int(self.numerator * (other.denominator / self.denominator))

                    return f"{other.numerator + new_numerator}/{other.denominator}"
            else:
                common_denominator = max(self.denominator, other.denominator)
                while True:
                    common_denominator += 1
                    if all(common_denominator % d == 0 for d in [self.denominator, other.denominator]):
                        break
                k1 = int(common_denominator / self.denominator)
                k2 = int(common_denominator / other.denominator)

                return f"{k1 * self.numerator + k2 * other.numerator}/{common_denominator}"
        else:
            return f"{self.numerator + other.numerator}/{self.denominator}"

# код для проверки 
fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
