class Animal :
    def eat(self):
        print("Animal is eating")

class Dog :
    def eat(self):
        print("Dog is eating")

class Cat :
    def eat(self):
        print("Cat is eating")

c = Cat()
d = Dog()
a = Animal()

c.eat()
d.eat()
a.eat()

# polymorphism using inheritance