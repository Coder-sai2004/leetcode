# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
        c=head
        d=ListNode(0)
        t=d
        while c:
            if c.val not in s:
                t.next=ListNode(c.val)
                t=t.next 
            c=c.next
        return d.next