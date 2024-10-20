class Animal :
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(self.name + " animal is eating")

class Dog(Animal):
    def __init__(self,name,type):

        # call the contructor/initilizer of animal class
        Animal.__init__(self,name)
        self.type = type

dog = Dog("moti","dobberman")
dog.eat()