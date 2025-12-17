# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        x,res,j=[],[],0
        while head:
            x.append(head.val)
            head=head.next
        n=len(x)//k
        for _ in range(n):
            a=x[j:j+k][::-1]
            res.extend(a)
            j+=k
        res.extend(x[j:])
        dummy=ListNode(0)
        cur=dummy
        for i in res:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next