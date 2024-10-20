def merge_sort(arr, left_half, right_half):
    i = j = k = 0

    while i<len(left_half) and j<len(right_half):
        if left_half[i]<right_half[j]:
            arr[k] = left_half[i]
            i +=1

        else:
            arr[k] = right_half[j]
            j +=1
        k += 1

    while i < len(left_half):
        arr[k] = left_half
        i += 1
        k += 1

    while j <len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

arr = [2,3,7,7] 


print(merge_sort)