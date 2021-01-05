def CountingSort1(arr):
    #finding the maximum array size
    max1=0
    l=[]
    for i in range(len(arr)):
        if max1<arr[i]:
            max1=arr[i]
    #creating an array with size max1
    for i in range(max1+1):
        l.append(0)
    #counting occurence of each number
    for i in range(len(arr)):
        l[arr[i]]+=1
        
    #printing the result
    for i in range(len(l)):
        for j in range(l[i]):
            print(i,end=" ")
CountingSort1([4,3,2,2,1])

      

    
    
    
