class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memoize = [0 for x in range(len(arr))]      #dynamic programming
        maximum = 0
        for curr_pos in range(len(arr)):
            self.dfs(curr_pos,arr,d,memoize)        #go as far as we can go
            maximum = max(maximum,memoize[curr_pos])        #we can't go anymore so compare result 
        return maximum

    def dfs(self,curr_pos,arr,d,memoize):
        if memoize[curr_pos] != 0:      #if seen before, get it from dp
            return 1 + memoize[curr_pos]
        for next_move in range(1,d + 1):    #move backward and use dp
            if curr_pos - next_move >= 0 and arr[curr_pos] > arr[curr_pos - next_move]:
                memoize[curr_pos] = max(memoize[curr_pos],memoize[curr_pos - next_move] + 1)
            else:
                break
        for next_move in range(1,d + 1): #move forward and check if u can move further
            new_pos = curr_pos + next_move
            if 0 <= new_pos < len(arr) and arr[curr_pos] > arr[new_pos]:    #valid range
                memoize[curr_pos] = max(memoize[curr_pos],self.dfs(new_pos,arr,d,memoize) + 1)
            else:   #no more forward movement
                memoize[curr_pos] = max(memoize[curr_pos],1) 
                return memoize[curr_pos]
        return memoize[curr_pos] 
        
        
            
            
