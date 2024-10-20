def push_zeros_to_end(arr) :
    count = 0
    n= len(arr)
    temp = [0]*n

    for i in range (n) :
        if (arr[i] !=0):
            temp[count]=arr[i]
            count +=1

    while(count<n):
        temp[count] = 0
        count +=1

    for i in range(n):
        arr[i] = temp[i]

arr = [1,2,0,4,3,0,5,0]
push_zeros_to_end(arr)
print(arr)