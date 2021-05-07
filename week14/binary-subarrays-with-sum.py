class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        counter = defaultdict(lambda : 0)
        counter[0] = 1
        current_sum = 0
        answer = 0
        for num in A:
            current_sum += num
            diff = current_sum - S
            if diff in counter:
                answer += counter[diff]
            counter[current_sum] += 1
        return answer
            
        
