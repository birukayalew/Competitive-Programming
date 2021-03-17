class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = {}
        for word in strs:
            
            temp = [0 for i in range(26)]
            for letter in word:
                temp[ord(letter)-ord('a')] += 1
                
            list_to_tuple = tuple(temp)
            if list_to_tuple in anagram:
                anagram[list_to_tuple].append(word)
            else:
                anagram[list_to_tuple] = [word]
        return list(anagram.values())
