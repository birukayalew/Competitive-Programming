# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        start_index = 0
        end_index = 0
        start = ans = head
        while head:
            if (end_index - start_index) == n:
                if head.next:
                    start = start.next
                    start_index += 1
                else:
                    start.next = start.next.next
                    return ans
            head = head.next  
            end_index += 1
        if start == ans:
            ans = start.next
        return ans  
