def binary_serch(arr,target):
    # initilise
    low = 0
    high = len(arr)-1

    while low<=high :
        # calculate mid

        mid = (low+high)//2
        if arr[mid]==target: #compare
            return mid
        elif arr[mid]<target:
            low = mid+1
            # adjust low/high
        
        else:
            high = mid-1
    return-1