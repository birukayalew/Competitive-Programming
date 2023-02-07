class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        visited = set()
        curr_dir = (0, 1)
        pos = (0, 0)
        for i in range(4):
            for inst in instructions:
                if pos == (0, 0):
                    visited = set()
                posx, posy =  pos
                x, y = curr_dir
                if inst == "G":
                    pos = (posx + x, posy + y)
                    visited.add(pos)
                elif inst == "L":
                    x, y = -y, x
                    curr_dir = (x, y)
                else:
                    x, y = y, -x
                    curr_dir = (x, y)
                    
                    
        if pos == (0, 0):
            visited = set()
                    
        return len(visited) == 0