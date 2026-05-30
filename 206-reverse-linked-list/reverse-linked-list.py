# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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