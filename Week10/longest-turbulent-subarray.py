class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        start = 0
        end = 0
        less_than = True
        greater_than = True
        maximum_size = 1
        while end < len(arr) - 1:
            if greater_than and arr[end] > arr[end + 1]: 
                greater_than = False         #next round greater than is not allowed
                less_than = True
                end += 1
            elif less_than and arr[end] < arr[end + 1]:
                less_than = False            #next round less than is not allowed
                greater_than = True
                end += 1
            else:
                maximum_size = max(maximum_size,end - start + 1) 
                start += 1
                end = start
                less_than = True       #start from new (can be both greater than or less than)
                greater_than = True
            
        return max(maximum_size,end - start + 1)
