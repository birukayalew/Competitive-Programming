class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(string):
            n = len(string)
            for i in range(n // 2):
                if string[i] != string[n - i - 1]:
                    return False
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return check_palindrome(s[l:r]) or check_palindrome(s[l + 1:r + 1]) 
            l += 1
            r -= 1
        return True            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        