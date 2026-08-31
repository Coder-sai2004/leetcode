# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res=[]
        pre=head
        cur=head.next
        idx=1
        while cur.next:
            if (pre.val<cur.val and cur.next.val<cur.val) or (pre.val>cur.val and cur.next.val>cur.val):
                res.append(idx)
            idx+=1
            pre=pre.next
            cur=cur.next
        if len(res)<2:
            return [-1,-1]
        mi=float('inf')
        mx=res[-1]-res[0]
        for i in range(1,len(res)):
            mi=min(mi,(res[i]-res[i-1]))
        return [mi,mx]