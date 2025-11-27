# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        l2=[]
        c=list1
        d=list2
        while c:
            l1.append(c.val)
            c=c.next
        while d:
            l2.append(d.val)
            d=d.next
        dummy=ListNode()
        cur=dummy
        x=l1+l2
        y=sorted(x)
        for val in y:
            cur.next=ListNode(val)
            cur=cur.next
        return dummy.next

        