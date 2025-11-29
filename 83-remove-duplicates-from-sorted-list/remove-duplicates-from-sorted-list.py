# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r=[]
        while head:
            r.append(head.val)
            head=head.next
        s=set(r)
        l=sorted(list(s))
        dummy=ListNode(0)
        cur=dummy
        for i in l:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next