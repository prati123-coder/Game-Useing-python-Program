class Person :
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.__salary = salary

        def findAge(self):
            return self.age 
        
        def getSalary(self):
            print(self.__salary)
        
per = Person("prerana",21,100000)

print(per.name)

per.getSalary()

print(per.__salary)
