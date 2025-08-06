"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод get_set_del, 
в котором происходи получение, присваивание и удаление значения.
"""


class Car:
    brand: str
    model: str
    release_year: int

    def __init__(self, brand, model, release_year):
        self.brand = brand
        self.model = model
        self.release_year = release_year

    def get_set_del(self):
        self.release_year += 1
        self.model = "Q7"
        del self.model

class CarSlots:
    __slots__ = ("brand", "model", "release_year")

    def __init__(self, brand, model, release_year):
        self.brand = brand
        self.model = model
        self.release_year = release_year

    def get_set_del(self):
        self.release_year += 1
        self.model = "Q7"
        del self.model


car = Car('Toyota', 'Corolla', 2022)
car_slots = CarSlots('Toyota', 'Crown', 1990)

import timeit

t1 = timeit.timeit(car.get_set_del)
t2 = timeit.timeit(car_slots.get_set_del)

print((t1-t2)/t1*100)
