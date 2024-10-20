def first_last(arr,x):
    first = -1
    last = -1

    for i in range(len(arr)):
        if (x !=arr[i]):
            continue

        if (first == -1):
            first = i

        last = i

    return [first, last]

arr = [1,4,4,4,44,55]
x=4
first_last(arr,x)