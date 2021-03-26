class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        intervals.sort(key = lambda x : x[1]) #sort by end
        count = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[0][1]: #if they overlap
                count += 1
            else:
                intervals[0] = intervals[i] #if not overlapped, update your current at index 0
        return count
