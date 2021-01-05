def InsertionSort(arr):
    for i in range(1,len(arr)):
        index=i
        while index>0:
            if arr[index]<arr[index-1]:
                arr[index],arr[index-1]=arr[index-1],arr[index]
                index-=1
            else:
                index-=1
    return arr
print(InsertionSort([1,1,4,4,5,6,7,0]))
        
