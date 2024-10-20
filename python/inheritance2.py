class Parent :
    property = 90

class child :
    property = 99

    def display(self):
        print("child property",self.property)
        print("parent property", super().property)

obj = child()
obj.display()