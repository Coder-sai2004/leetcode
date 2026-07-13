# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        h1=head
        h2=head.next
        while head:
            x=head.next
            if head.next:
                head.next=head.next.next
                head=x
            else:
                break
        ans=h1
        while h1.next:
            h1=h1.next
        h1.next=h2
        return ans