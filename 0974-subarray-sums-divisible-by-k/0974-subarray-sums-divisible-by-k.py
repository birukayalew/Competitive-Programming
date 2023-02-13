class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        remainders = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[i] + nums[i])
            
        for num in prefix_sum:
            modulo = num % k 
            if modulo in remainders:
                count += remainders[modulo]
            remainders[modulo] += 1
            
        return count