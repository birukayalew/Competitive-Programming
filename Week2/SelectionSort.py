def SelectionSort(arr):
    for i in range(len(arr)-1):
        min1=i
        for j in range(i+1,len(arr)):
            if arr[min1]>arr[j]:
                min1=j
        arr[i],arr[min1]=arr[min1],arr[i]
    return arr
print(SelectionSort([4,3,3,2,1]))
