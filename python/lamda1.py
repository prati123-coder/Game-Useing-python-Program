func = lambda x : x+10
print(func(5))

# second program of lambda

add = lambda a , b : a+b
print(add(5,6))

# nested function

def myFunc() :
    # return a new functio 
    return lambda msg : print(msg)
myFunc()("hello world")
