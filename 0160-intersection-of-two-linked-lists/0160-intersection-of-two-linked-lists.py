# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1 = len2 = 0
        nodeA, nodeB = headA, headB
        while nodeA:
            len1 += 1
            nodeA = nodeA.next
        while nodeB:
            len2 += 1
            nodeB = nodeB.next
        if len1 > len2:
            for i in range(len1 - len2):
                headA = headA.next
        elif len2 > len1:
            for i in range(len2 - len1):
                headB = headB.next
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return