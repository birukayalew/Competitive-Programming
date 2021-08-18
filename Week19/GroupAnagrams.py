class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []
        d = {}
        for i in range(len(strs)):
            temp = [0 for x in range(26)]
            for letter in strs[i]:
                temp[ord(letter) - ord('a')] += 1
            if tuple(temp) in d:
                d[tuple(temp)].append(strs[i])
            else:
                d[tuple(temp)] = [strs[i]]
        for key in d:
            ans.append(d[key])
        return ans
