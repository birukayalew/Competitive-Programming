class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]
        self.length = len(nums)
        for i in range(self.length - 1):
            self.prefix.append(self.prefix[i] + nums[i])
        
    def sumRange(self, left: int, right: int) -> int:
        
        return self.prefix[right] - self.prefix[left] + self.nums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
