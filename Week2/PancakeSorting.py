class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            currmax=i
            for j in range(i-1,-1,-1):
                if arr[j]>arr[currmax]:
                    currmax=j
            if currmax!=i:
                self.reverse(arr,currmax)
                self.reverse(arr,i)
                ans.append(currmax+1)
                ans.append(i+1)
        return ans
        
        
    def reverse(self,arr,back):
        front=0
        while front<back:
            arr[front],arr[back]=arr[back],arr[front]
            front+=1
            back-=1
        return arr
            
            
