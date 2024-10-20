def add_numbers(a : int,b : int)-> int :
    return a+b
print(add_numbers(5,6))


def outer() :
    print("hello from the outer")

def inner() :
    print("hello from inner")
    return inner
fn = outer()
