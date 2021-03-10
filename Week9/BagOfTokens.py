class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        
        result = 0 #maximum score so far
        score = 0 #current score
        #sliding window
        start = 0 #start index
        end = len(tokens)-1 #end index
        
        while start <= end and start < len(tokens):
            if P >= tokens[start]:
                P -= tokens[start]
                score += 1
                result = max(result,score)
                start += 1
            else:
                if score == 0:
                    return result
                else:
                    score -= 1
                    P += tokens[end]
                    end -= 1
                    result = max(result,score)
        return result
                
