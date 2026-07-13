# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        h1=None
        h2=None
        t1=None
        t2=None
        i=0
        while head:
            i+=1
            node=ListNode(head.val)
            if i%2!=0:
                if h1 is None:
                    h1=node
                    t1=node
                else:
                    t1.next=node
                    t1=node
            else:
                if h2 is None:
                    h2=node
                    t2=node
                else:
                    t2.next=node
                    t2=node
            head=head.next
        ans=h1
        while h1.next:
            h1=h1.next
        h1.next=h2
        return ans