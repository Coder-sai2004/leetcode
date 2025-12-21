# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        res=res[::-1]
        res.pop(n-1)
        res=res[::-1]
        dummy=ListNode(0)
        cur=dummy
        for i in res:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next