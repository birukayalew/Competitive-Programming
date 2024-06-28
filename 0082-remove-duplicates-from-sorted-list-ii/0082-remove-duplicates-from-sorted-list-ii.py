# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = defaultdict(int)
        ans = temp = head
        
        while head:
            d[head.val] += 1
            head = head.next
            
        while temp:
            if d[temp.val] > 1:
                temp.val = '#'
            temp = temp.next
            
        result = prev = ListNode(0)
        
        while ans:
            while ans and ans.val == '#':
                ans = ans.next
                
            prev.next = ans
            prev = ans
            if ans:
                ans = ans.next
            
        
        return result.next
            