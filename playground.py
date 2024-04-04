#
# def add(*args):
#     score = 0
#     for num in args:
#         score+=num
#
#     return score
#
# def calculate(n,**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# print(calculate(2, add=3,multiply=9))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
my_car = Car(make="Nissan")
print(my_car.make)