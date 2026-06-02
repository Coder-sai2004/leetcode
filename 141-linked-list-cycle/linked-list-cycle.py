# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while slow:
            slow=slow.next
            if fast.next is None or fast.next.next is None:
                return False
            fast=fast.next.next
            if slow==fast:
                return True