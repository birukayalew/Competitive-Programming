# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        g_set = set(G)
        counter = 0
        connected = False
        node = head
        while node:
            if node.val in g_set:
                connected = True
            else:
                if connected:
                    counter += 1
                    connected = False
            node = node.next
        if connected:
            return counter + 1
        return counter
            
            
                
                
