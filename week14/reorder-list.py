# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = []
        curr_node = head
        
        while curr_node:
            temp.append(curr_node)
            curr_node = curr_node.next
        start = 1
        end = len(temp) - 1
        
        while end > start:
            head.next = temp[end]
            head = head.next
            head.next = temp[start]
            head = head.next
            start += 1
            end -= 1
        head.next = temp[end]
        head.next.next = None
        
