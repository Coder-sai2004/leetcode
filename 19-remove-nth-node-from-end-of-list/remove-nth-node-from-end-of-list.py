# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        l=0
        #temp is calculate the size of linked list and dummy for finding the nth node
        temp=head
        dummy=head
        while temp:
            l+=1
            temp=temp.next
        #k refers to the nth node from the starting point of view
        k=l-n
        #if nth node is the starting node
        if i==k:
            return head.next
        else:
            while dummy:
                if i+1==k:
                    dummy.next=dummy.next.next
                    break
                dummy=dummy.next
                i+=1
        return head