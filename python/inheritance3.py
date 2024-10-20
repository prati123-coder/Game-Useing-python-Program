class Parent :
    property = 90

    def eat(self):
        print("parent eating")

class child(Parent):
    property = 99

    def display(self):
        print("child property",self.property)
        print("parent property",super().property)
    
    def eat(self):
        print("chil eatim]ng")

    def callEat(self):
        self.eat()
        super().eat()