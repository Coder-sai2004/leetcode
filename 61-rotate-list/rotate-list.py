# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        dummy=ListNode(0)
        cur=dummy
        if len(res)<1:
            return dummy.next
        n=k%len(res)
        x=len(res)-n
        r=res[x:]+res[:x]
        for i in r:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next