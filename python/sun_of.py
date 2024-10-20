def sum_of(arr,n):
    #base condition
    if n==0:
        return 0
    else:
        return sum_of(arr,n-1)+arr[n-1]
    
arr= [1,2,3,4,5]
print(sum_of(arr,len(arr)))