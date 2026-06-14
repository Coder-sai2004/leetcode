# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        st=[]
        n=0
        res=0
        i=0
        dummy=head
        #to find the length of linked list
        while dummy:
            n+=1
            dummy=dummy.next
        m=n//2
        #taking the values of first half of linked list into the stack
        while head:
            if i==m:
                break
            st.append(head.val)
            head=head.next
            i+=1
        #adding the values of second half of linked list to the stack values
        while head:
            x=head.val+st.pop()
            res=max(res,x)
            head=head.next
        return res