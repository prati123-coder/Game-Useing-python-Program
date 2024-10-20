class num :
    def __init__(self,num):
        self.num = num

    def __add__(self, u):
        return self.num + u.num
    
num1 = num(5)
num2 = num(30)

res = num1 +num2
print(res)