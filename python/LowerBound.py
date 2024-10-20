def lower_bound(arr, x):
    for i in range(len(arr)):
        if arr[i]>= x:
            return i 
    return i+1
a=[2,2,2,2,5,5,8]
x = 0
lower_bound(a,x)
print(lower_bound)