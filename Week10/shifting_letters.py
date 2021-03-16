class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        temp = 0
        answer = ""
        for i in range(len(shifts) - 1,-1,-1):
            temp += shifts[i]
            curr = ord(S[i]) - 97  + temp
            curr = (curr % 26) + ord('a')
            answer = chr(curr) + answer
        return answer
            
