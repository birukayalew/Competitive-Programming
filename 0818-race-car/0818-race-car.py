class Solution:
    def racecar(self, target: int) -> int:
        visited = set((1,0))
        # speed,position,length
        q = deque([(1,0,0)])
        
        while q:
            sp,pos,length = q.popleft()
            
            if pos == target:
                return length
            
            if not(sp < 0 and pos < 0):
                # Accelerate
                A_pos = pos + sp
                A_sp = sp * 2
                # Reverse
                R_pos = pos
                R_sp = -1 if sp >= 0 else 1
                
                if (A_sp,A_pos) not in visited:
                    q.append((A_sp,A_pos,length + 1))
                    visited.add((A_sp,A_pos))
                if (R_sp,R_pos) not in visited:
                    q.append((R_sp,R_pos,length + 1))
                    visited.add((R_sp,R_pos))