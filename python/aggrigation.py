# has aggrigation 

class Car :
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

class Person :
    def __init__(self,name,car):
        self.name = name
        self.car = car

car = Car("BMW","black")
person = Person("pratiksha",car)