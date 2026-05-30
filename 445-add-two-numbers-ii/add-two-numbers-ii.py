# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if head and head.next:
            tail=head
            head=head.next
            tail.next=None
        else:
            return head
        while head:
            x=head.next
            head.next=tail
            tail=head
            head=x
        return tail

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1=self.reverse(l1)
        h2=self.reverse(l2)
        head = None
        tail = None
        b = 0
        s = 0
        
        while h1 or h2:
            if h1 and h2:
                s = h1.val + h2.val + b
                h1 = h1.next
                h2 = h2.next
            elif h1:
                s = h1.val + b
                h1 = h1.next
            elif h2:
                s = h2.val + b
                h2 = h2.next
        
            n = s % 10
            b = s // 10
        
            node = ListNode(n)
        
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node
        
        if b > 0:
            node = ListNode(b)
            tail.next = node
            tail = node
        
        res=self.reverse(head)
        while res:
            if res.val==0 and res.next is None:
                return res
            elif res.val==0:
                res=res.next
            else:
                return res