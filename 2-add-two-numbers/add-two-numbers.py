# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=None
        tail=None
        b=0
        s=0
        while l1 or l2:
            if l1 and l2:
                s=l1.val+l2.val+b
                l1=l1.next
                l2=l2.next
            elif l1:
                s=l1.val+b
                l1=l1.next
            elif l2:
                s=l2.val+b
                l2=l2.next
            
            n=s%10
            b=s//10
            node=ListNode(n)
            if head is None:
                head=node
                tail=node
            else:
                tail.next=node
                tail=node
        if b>0:
            node=ListNode(b)
            tail.next=node
            tail=node
        return head