class ComplexNum :
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self,c):
        return self.x + c.x , self.y + c.y
    
c1 = ComplexNum(2,5)
c2 = ComplexNum(3,6)

print(c1+c2)