from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = defaultdict(lambda:0)
        answer = []
        result = 0
        for num in arr:
            d[num] += 1
        for key in d:
            answer.append(d[key])
        answer.sort()
        length = len(arr)
        for i in range(len(answer) - 1, -1, -1):
            length -= answer[i]
            result += 1
            if length <= len(arr) / 2:
                return result
            
        return result
