class Calculator :
    def add(self,a,b):
        return a+b      # avodie this function get error
    def add(self,a,b,c):
        return a+b+c
cal = Calculator()  
print(cal.add(5,6,7))