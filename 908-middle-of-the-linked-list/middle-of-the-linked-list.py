# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        n=0
        while dummy:
            n+=1
            dummy=dummy.next
        m=n//2
        i=0
        while head:
            if i==m:
                return head
            head=head.next
            i+=1