# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        #calculating the size of linked list
        dummy=head
        n=0
        while dummy:
            n+=1
            dummy=dummy.next

        #middle node position    
        idx=n//2
        
        i=0
        result=head
        pre=head
        head=head.next
        while head:
            i+=1
            if idx==i:
                pre.next=pre.next.next
                break
            pre=pre.next
            head=head.next
        return result