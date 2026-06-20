# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middle(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow


    def merge(self,left,right):
        dummy=ListNode(0)
        tail=dummy

        while left and right:
            if left.val<=right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next

            tail=tail.next

        if left:
            tail.next=left

        if right:
            tail.next=right

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        m=self.middle(head)
        
        right_half=m.next
        m.next=None

        left=self.sortList(head)
        right=self.sortList(right_half)

        return self.merge(left,right)