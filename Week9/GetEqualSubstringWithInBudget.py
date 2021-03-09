class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = []
        max_length_container = []
        max_length = 0
        curr_sum = 0
        start_index = 0
        for i in range(len(s)):
            absolute_diff = abs(ord(s[i]) - ord(t[i]))
            diff.append(absolute_diff)
        for i in range(len(diff)):
            curr_sum += diff[i]
            if curr_sum <= maxCost:
                max_length += 1
                max_length_container.append(max_length)
            else:
                
                while curr_sum > maxCost:
                    curr_sum -= diff[start_index]
                    start_index += 1
                    max_length_container.append(max_length)
                    max_length -= 1
                max_length += 1  
        return max(max_length_container)
