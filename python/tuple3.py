names = ("pratiksha","prerana","priti","pratiksha","prerana")
print(names.count("prerana"))

print(names.count("ganesh"))

#index method

print(names.index("pratiksha"))    # it is defined first word


print(len(names))      # to find lengh of the tuple

print(names[3])

print(names[-2])

names[3]="ganesh"      # tuple is immutable
print(names)