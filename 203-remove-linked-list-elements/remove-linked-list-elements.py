# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        x=[]
        while head:
            x.append(head.val)
            head=head.next
        c=x.count(val)
        j=0
        i=0
        while j<c:
            if x[i]==val:
                x.remove(val)
                j+=1
                continue
            i+=1
        dummy=ListNode(0)
        cur=dummy
        for i in x:
            cur.next=ListNode(i)
            cur=cur.next
        return dummy.next