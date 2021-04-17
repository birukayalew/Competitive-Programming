class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        q = deque()
        dp = {}
        q.append((0,0,2))
        minimum = float('inf')
        
        while q:
            side_jumps,point,lane=q.popleft()
            
            while point < n and obstacles[point] != lane:   #go as far as u can
                point += 1
                
            point -= 1   
            if point == n - 1:   #if u reached to ur destination(n), boom!!!
                return side_jumps
            
            for newlane in (1,2,3):
                if obstacles[point] != newlane and obstacles[point + 1] != newlane: #means there is side jump
                    if (point,newlane) in dp: #we've seen it
                        if side_jumps + 1 > dp[(point,newlane)]: #if this side jump is not the smallest at this point and lane
                            minimum = min(minimum,dp[(point,newlane)])
                        else:
                            dp[(point,newlane)] = side_jumps + 1 #update smallest jump
                    else:
                        dp[(point,newlane)] = side_jumps + 1
                        q.append((side_jumps + 1,point,newlane))
                        minimum = min(minimum,side_jumps + 1)
                        
        return minimum
        
        
