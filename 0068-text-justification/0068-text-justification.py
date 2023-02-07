class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        numChars, cur, res = 0, [], []
        for word in words:
            if numChars + len(word) + len(cur) <= maxWidth: 
                numChars += len(word)
                cur.append(word)
            else:                                          
                quotient, remainder = divmod(maxWidth-numChars, len(cur)-1 or 1) 
                for i in range(len(cur)-1) or [0]:
                    cur[i] += " "*(quotient+(remainder > 0))     
                    remainder -= 1
                res.append(''.join(cur))                  
                numChars, cur = len(word), [word]                     
        res.append(' '.join(cur)+" "*(maxWidth-numChars-len(cur)+1)) 
        return res