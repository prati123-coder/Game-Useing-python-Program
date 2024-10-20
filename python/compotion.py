class Engine :
    def engineDetails(self):
        print("car engin is model e1213")

class Tyres :
    def tyresDetails(self):
        print("car tyres is apollo")

class Door :
    def doorDetails(self):
        print("Doors of the car is automatic")


class Car :
    def __init__(self):

       self.engine = Engine()
       self.tyres = Tyres()
       self.door = Door()

    def printDetails(self):
      self.engineDetails()
      self.tyres.tyresDetails()
      self.door.doorDetails()

c = Car()
c.printDetails()