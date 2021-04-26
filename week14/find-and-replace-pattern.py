class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            check = {}
            used = set()
            match = True
            for i in range(len(pattern)):
                if pattern[i] not in check:
                    if word[i] in used:
                        match = False
                        break
                    else:
                        check[pattern[i]] = word[i]
                        used.add(word[i])
                else:
                    if word[i] != check[pattern[i]]:
                        match = False
                        break
            if match:
                ans.append(word)
        return ans
            
