# Write a python program to check if a number is prime or not prime

num = int(input("enter a number"))

isPrime = True
if(num <=1):
    isPrime = False

for i in range(2,int(num/2)+1):
   if num%i==0 :
     isPrime = False
     break
   print("number passed is prime :",isPrime)