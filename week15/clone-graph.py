"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        store = {}
        self.dfs(node,store)
        if node:
            return store[node.val]
        return node
        
        
        
        
    def dfs(self,node,store):
        if not node:
            return
        
        if node.val not in store:
            new_node = Node(node.val)
            store[new_node.val] = new_node
        else:
            new_node = store[node.val]
        
        for neighbor in node.neighbors:
            if neighbor.val in store:
                new_node.neighbors.append(store[neighbor.val])
            else:
                curr = Node(neighbor.val)
                new_node.neighbors.append(curr)
                store[neighbor.val] = curr
                self.dfs(neighbor,store)
        
                
               
