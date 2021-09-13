# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Iterative way
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans=ListNode(0)
        v1=0
        while head:
            v1=head.val
            head=head.next
            newNode=ListNode(v1)
            if ans.next==None:
                ans.next=newNode
                newNode.next=None
            else:
                curr=ans.next
                ans.next=newNode
                newNode.next=curr
        return ans.next
#Recursive way
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.result = None
        if head==None:
            return head
        self.reverse(head)
        return self.result
        
        
    def reverse(self,head: ListNode):
        if head.next == None:
            self.result=head
            return head
        
        rev = self.reverse(head.next)
        rev.next = head
        head.next = None
        return head
        
        
        
        
