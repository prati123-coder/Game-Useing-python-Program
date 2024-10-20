def binary_serch(arr,left,right,target):
    if left>right:
        return-1
    mid = left+(right-left)//2

    if arr[mid]==target:
        return mid
    
    elif arr[mid]>target:

        return binary_serch(arr,left,mid-1,target)
    
    else:
        return binary_serch(arr,mid+1,right,target)
    
arr = [2,3,4,6,10,30]
target = 10

print(binary_serch(arr,0,len(arr)-1,target))