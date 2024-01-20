class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bucket_size = valueDiff + 1
        buckets = {}

        for i in range(len(nums)):
            bucket_id = nums[i] // bucket_size
            for bid in (bucket_id - 1, bucket_id, bucket_id + 1):
                if bid in buckets:
                    for x, j in buckets[bid]:
                        if abs(nums[i] - x) <= valueDiff and abs(i - j) <= indexDiff:
                            return True
            buckets.setdefault(bucket_id, []).append((nums[i], i))

        return False