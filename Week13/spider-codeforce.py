#the basic algorithm is to find the maximum connected threads in each spider
#and then adding them will give us the longest spider(the answer)

from collections import defaultdict,deque
with open('input.txt') as f:
    lines = f.readlines()
    
max_length = 0   #the length of the expected spider
def bfs(graph,bead,visited):  # this will find length of connected beads
    q = deque()
    q.append((0,bead))  #number of threads connected to current bead, bead 
    while q:
        connected_threads,bead = q.popleft()
        visited.add(bead)
        for neighbours in graph[bead]:
            if neighbours not in visited:
                visited.add(neighbours)
                q.append((connected_threads + 1,neighbours)) 
    return connected_threads  # max number of connections to the this bead

for line in lines[1:]: # don't need number of beads([1:])
    local_length = 0  #compares possible connections per spider
    graph = defaultdict(list)
    line = line.rstrip("\n").split(" ")  #removing newline
    index = 1  
    while index < len(line):  #building undirected graph per spider
        graph[line[index]].append(line[index + 1])   
        graph[line[index + 1]].append(line[index])
        index += 2
    for key in graph:
        if len(graph[key]) == 1:  #start from beads which are tails to get max connection
            visited = set()
            res = bfs(graph,key,visited)
            local_length = max(local_length,res)
    max_length = max_length + local_length  #then add max connections per spider to our result
    
f = open("output.txt", "a")
f.write(f'{max_length}')
f.close()
