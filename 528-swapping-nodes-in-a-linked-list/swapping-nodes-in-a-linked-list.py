# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        i=0
        j=0
        dummy=head
        temp=head
        res=head
        #finding the size of linked list
        while dummy:
            n+=1
            dummy=dummy.next
        end=(n-k)+1
        #finding the kth node from the beginning
        while temp:
            i+=1
            if i==k:
                x=temp
                break
            temp=temp.next
        #finding kth node from end and swapping it.
        while head:
            j+=1
            if j==end:
                head.val,x.val=x.val,head.val
            head=head.next
        return res