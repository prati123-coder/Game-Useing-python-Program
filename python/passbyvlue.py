num = 5

def modify_num(num):
    num +=1
    print(num)

modify_num(num)

print("original num",num)

# immutable data types: numbers,string,tuole --passed by value

# pss by refernce : mutable datatypes: list, divtionary


# pass by refernce

my_list = [1,2,4]
def modify_list(li):
    li.append(5)
    print(li)

print("before calling fun", my_list)

modify_list(my_list)
print("after calling fun",my_list)