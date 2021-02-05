import heapq as h
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.k=k
        for i in range(len(nums)):
            if i < self.k:
                h.heappush(self.heap,nums[i])
            else:
                poped = h.heappop(self.heap)
                if nums[i] > poped:
                    h.heappush(self.heap,nums[i])
                else:
                    h.heappush(self.heap,poped)

    def add(self, val: int) -> int:
        if len(self.heap) == 0:
            h.heappush(self.heap,val)
        if len(self.heap)<self.k:
            h.heappush(self.heap,val)
            poped = h.heappop(self.heap)
            h.heappush(self.heap,poped)
        else:
            poped = h.heappop(self.heap)
            if val > poped:
                h.heappush(self.heap,val)
                poped = h.heappop(self.heap)
                h.heappush(self.heap,poped)
            else:
                h.heappush(self.heap,poped)
            
        return poped
            
            
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
