import heapq as h
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        repetitions = {}
        heap=[]
        ans=[]
        for num in words:
            if num in repetitions:
                repetitions[num][0]+=1
            else:
                repetitions[num]=[1,num]
        for key in repetitions:
            h.heappush(heap,[-1*repetitions[key][0],repetitions[key][1]])
        for i in range(k):
            ans.append(h.heappop(heap)[1])
        return ans
            
