import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=head
        tail=head
        head=head.next
        while head:
            #calculating gcd of two adjacent values
            m=math.gcd(tail.val,head.val)
            node=ListNode(m)
            #inserting the new node between the nodes
            tail.next=node
            node.next=head
            #moving forward
            tail=head
            head=head.next
        return res