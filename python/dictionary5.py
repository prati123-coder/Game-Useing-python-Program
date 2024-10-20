students_details = {'name':"pratiksha",'age':21,'city':"solapur"}
marks_details = {'english':100,'maths':78,'science':92}

students_details.update(marks_details)  # two dictionary add
print(students_details)

# how to remove the elements from the the dictionary

print(students_details.pop('city'))      #using pop funtion
print(students_details)

# clear method
students_details.clear()
print(students_details)    # empty dictionary

