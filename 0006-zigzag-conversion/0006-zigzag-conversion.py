class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        temp = defaultdict(list)
        idx, step = 0, 0
        while idx < len(s):
            if step >= numRows:
                step -= 2
                while idx < len(s) and step >= 0:
                    temp[step].append(s[idx])
                    idx += 1
                    step -= 1
                step = 1
            else: 
                temp[step].append(s[idx])
                step += 1
                idx += 1
        
        merged_list = list(itertools.chain(*temp.values()))
        return "".join(merged_list)
        