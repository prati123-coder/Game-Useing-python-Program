class Person :
    def __init__(self,name,car):
        self.__name = name
        self.__car = car

        # getters and setters- public method to allow the controlled interaction

    def getNmae(self):
        return self.__name
    def setName(self,name):
        self.__name = name

    def getCar(self):
        return self.__car
    def setCar(self,car):
        self.__car = car
per = Person("pratiksha",21)

print(per.getName())
per.setName("pratiksha aware")
print(per.getName())