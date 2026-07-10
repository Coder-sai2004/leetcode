# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st=[]
        while head:
            #popping the nodes with greater value on its right side
            while st and head.val>st[-1].val:
                st.pop()
            #adding the nodes individually into the stack
            x=head.next
            head.next=None
            st.append(head)
            head=x
        #connecting the modified nodes in sequence
        for i in range(len(st)-1):
            st[i].next=st[i+1]
        return st[0]