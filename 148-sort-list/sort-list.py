# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        res.sort()
        new=None
        tail=None
        for i in res:
            node=ListNode(i)
            if new is None:
                new=node
                tail=node
            else:
                tail.next=node
                tail=tail.next
        return new