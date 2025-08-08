"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
import datetime


class Car:

    def __init__(self, brand: str, model: str, release_year: int):
        if release_year > datetime.datetime.now().year:
            raise Exception('Эта машина еще не была выпущена')
        else:
            self.brand = brand
            self.model = model
            self.release_year = release_year

# код для проверки
car = Car('Toyota', 'Corolla', 2022)

car = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')
