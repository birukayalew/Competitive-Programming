class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        max_distance = 1
        curr_distance = 0
        one_is_seen = False
        for i in range(len(seats)):
            if seats[i] == 1:
                if one_is_seen:
                    max_distance = max(max_distance, (curr_distance + 1) // 2)
                else:
                    max_distance = max(max_distance, curr_distance)
                    one_is_seen = True
                curr_distance = 0
            else:
                curr_distance += 1
        if curr_distance:
            max_distance = max(max_distance, curr_distance)
        return max_distance
