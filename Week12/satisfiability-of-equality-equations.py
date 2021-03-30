class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        leader = [x for x in range(26)]
        size = [1 for x in range(26)]
        def find(letter):
            l = ord(letter) - ord('a')
            if l == leader[l]:
                return l 
            leader[l] = find(chr(leader[l] + ord('a')))
            return leader[l]
        
        def union(letter1,letter2):
            letter1_leader = find(letter1)
            letter2_leader = find(letter2)
            if (size[letter2_leader] > size[letter1_leader]):
                leader[letter1_leader] = letter2_leader
                size[letter2_leader] += size[letter1_leader]
            else:
                leader[letter2_leader] = letter1_leader
                size[letter1_leader] += size[letter2_leader]
                
            
            
            
        for equation in equations:
            x,y = equation[0],equation[-1]
            if equation[1] == '=':
                union(x,y)
        for equation in equations:
            x,y = equation[0],equation[-1]
            if equation[1] == '!':
                x_leader = find(x)
                y_leader = find(y)
                if x_leader == y_leader:
                    return False
                
        return True
