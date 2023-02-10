class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        tail_index = dict()
        target_len = len(target)
        for x in nums:
            x_len = len(x)
            if x_len < target_len:
                if target[-x_len:] == x:
                    try:
                        tail_index[x_len] += 1
                    except KeyError:
                        tail_index[x_len] = 1
        
        
        if target_len & 1:
            symmetric = False
        else:
            htarget_len = target_len >> 1
            symmetric = target[:htarget_len] == target[htarget_len:]
        result = 0
        for x in nums:
            x_len = len(x)
            if x_len < target_len and target[:x_len] == x:
                comp_x_len = target_len - x_len
                try:
                    result += tail_index[comp_x_len]
                except KeyError:
                    pass
                if  x_len == comp_x_len and symmetric:
                    result -= 1
        return result