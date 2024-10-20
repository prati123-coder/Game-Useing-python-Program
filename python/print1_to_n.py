def print_numbers(n):
    #base condition
    if n>0:
        print_numbers(n-1)
        print(n)
print_numbers(6)