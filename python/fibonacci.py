n = int (input("Enter the value of n_ upto which we want the fibonacci series"))

if(n<=0):
    print("Number entered is not correct, it should be > 0. Entered num",n)

print(1, end=",")
if(n==1):
    pass
else:
    print(1, end=",") 
    if(n==2):
        pass
    else:
        # print the remaining part of the series
        prev = 1
        prev_prev=1
        for num in range(3, n+1):
            print(prev+prev_prev, end=",")
            prev, prev_prev = prev+prev_prev , prev


            #write a orogram to print the fibonacci  series up to n terms