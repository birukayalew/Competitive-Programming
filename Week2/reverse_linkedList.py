# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        if not head:
            return None
        while head:
            ans.append(head)
            head = head.next
        for i in range(len(ans) - 1,-1,-1):
            if i != 0:
                ans[i - 1].next = None
                ans[i].next = ans[i - 1]
                
        return ans[-1]
        
        
#recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.result = None
        if not head:
            return None
        
        self.rev(head)
        return self.result
    
    def rev(self,head):
        if not head.next:
            self.result = head
            return head
        
        curr = self.rev(head.next)
        curr.next = head
        head.next = None
        return head
