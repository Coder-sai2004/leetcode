# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        res=dummy
        while dummy and dummy.next and dummy.next.next:
            x=dummy.next
            y=dummy.next.next
            z = None if dummy.next.next.next is None else dummy.next.next.next

            dummy.next=y
            y.next=x
            x.next=z
            dummy=dummy.next.next
            
        return res.next