def CountingSort1(arr):
    #finding the maximum array size
    max1=0
    l=[]
    s=""
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
            print(s+str(i),end=" ")
    return s.rstrip(' ')
#print(CountingSort1([4,3,2,2,1]))
result=CountingSort1([4,3,2,2,1])
ans=' '.join(map(int, int(result)))
print(ans)
      

    
    
    
