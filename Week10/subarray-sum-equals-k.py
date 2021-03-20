class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        counter = 0 # number of continous subarrays
        current_sum = 0
        sum_container = defaultdict(lambda : 0)
        sum_container[0] = 1
        
        for num in nums:
            current_sum += num
            if (current_sum - k) in sum_container: #if complement of current sum is found, then subarray found
                counter += sum_container[current_sum - k]
            sum_container[current_sum] += 1
        return counter
