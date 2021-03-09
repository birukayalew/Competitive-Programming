class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        checker = set()
        counter = {}
        for i in range(len(arr)):
            if arr[i] in counter:
                counter[arr[i]] += 1
            else:
                counter[arr[i]] = 1
        for key in counter:
            checker.add(counter[key])
        if len(checker) < len(counter):
            return False
        return True
