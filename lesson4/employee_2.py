"""
Для класса Employee и Client, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee

"""
from typing import Union


class Employee:

    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        if issubclass(type(other), Employee):
            return self.pay + other.pay
        elif type(other) is int:
            return self.pay + other
        else:
            return 0


class Client:

    def __init__(self, pay):
        self.pay = pay

    def __add__(self, other):
        return 0 + other


class Developer(Employee):
    pass


class Manager(Employee):
    pass

# код для проверки
users = [Employee(50000), Client(100000), Developer(50000), Manager(50000)]

total_salary = 0
for user in users:
    total_salary = user + total_salary

print(total_salary)
# Вывод: 150000
