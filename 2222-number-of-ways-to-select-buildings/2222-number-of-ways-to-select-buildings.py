class Solution:
    def numberOfWays(self, s: str) -> int:
        number_10 = defaultdict(int)
        number_01 = defaultdict(int)
        number_101 = number_010 = count_0 = count_1 = cur_01 = cur_10 = 0
        for i in range(len(s)):
            if s[i] == '1':
                count_1 += 1
                number_01[i] = count_0 + cur_01
                cur_01 = number_01[i]
                number_10[i] = cur_10
                
            if s[i] == '0':
                count_0 += 1
                number_10[i] = count_1 + cur_10
                cur_10 = number_10[i]
                number_01[i] = cur_01
                
        for i in range(len(s)):
            if s[i] == '1':
                number_101 += number_10[i]
            else:
                number_010 += number_01[i]
                
        return number_101 + number_010
