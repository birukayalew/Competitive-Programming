class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        curr_sum = shifts[-1]
        self.next_letter(s[-1],curr_sum,shifts,-1)
        for i in range(len(s) - 2,-1,-1):
            curr_sum += shifts[i]
            self.next_letter(s[i],curr_sum,shifts,i)
            
        return "".join(shifts)
    
    def next_letter(self,letter,curr_sum,shifts,i):
        res = ord(letter) + (curr_sum % 26)
        if res > ord('z'):
            res = res % ord('z')
            shifts[i] = chr(ord('a') + res - 1)
        else:
            shifts[i] = chr(res)
        
