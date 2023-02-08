class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        con = defaultdict(list)
        for i,j in adjacentPairs:
            con[i].append(j)
            con[j].append(i)
        res = []  
        for i in con:           
            if len(con[i]) == 1:
                res.append(i)
                res.append(con[i][0])
                con.pop(i)
                break 
        for i in con:           
            if len(con[i]) == 1:
                con.pop(i)
                break 
        while con: 
            tmp = res[-1]
            fir = con[res[-1]][0]
            sec = con[res[-1]][1]
            if res[-2] == fir:
                res.append(sec)
            elif res[-2] == sec:
                res.append(fir)
            con.pop(tmp)
    
        return res