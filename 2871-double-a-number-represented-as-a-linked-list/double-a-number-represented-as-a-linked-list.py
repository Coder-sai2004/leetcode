# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #reversing the linked list
    def reverse(self,head):
        if head is None or head.next is None:
            return head
        else:
            tail=head
            head=head.next
            tail.next=None

        while head:
            x=head.next
            head.next=tail
            tail=head
            head=x

        return tail
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp=self.reverse(head)
        res=temp
        dummy=temp
        #multiplying every node value with 2
        while temp:
            temp.val*=2
            temp=temp.next
        #now here we are adding the carry to its next node
        carry=0
        while res:
            res.val+=carry
            carry=res.val//10
            res.val%=10
            if res.next is None:
                x=res
            res=res.next
            
        if carry>0:
            node=ListNode(carry)
            x.next=node
        #reversing the linkedlist to get the required result
        ans=self.reverse(dummy)
        return ans