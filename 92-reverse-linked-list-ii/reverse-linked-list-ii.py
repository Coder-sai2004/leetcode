# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #function used to reverse the linked list from the given positions
    def reverse(self,head,d):
        t=0
        if head and head.next:
                tail=head
                head=head.next
                tail.next=None
        else:
            return head,head
        while head and t<d:
            x=head.next
            head.next=tail
            tail=head
            head=x
            t+=1
        return tail,head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #n and dummy is for getting size of linkedlist
        n=0
        dummy=head
        while dummy:
            n+=1
            dummy=dummy.next

        #if it is a single node
        if head and head.next is None:
            return head

        ##d is for how much of length of linked list we are gonna reverse
        d=right-left

        #if left and right are the end postions of linked list
        if left==1 and right==n:
            x=self.reverse(head,d)
            return x[0]

        #if left is starting postion and right is in the middle
        elif left==1 and right!=n:
            t1=head
            x=self.reverse(head,d)
            t1.next=x[1]
            return x[0]

        #if left is not the starting position,we need to find the node where the actual reverse occur,so up until that we move forward
        elif left!=1:
            i=0
            temp=head
            while head:
                i+=1
                #left position found,so take left and prevoius position nodes to link it later
                if i==left-1:
                    t1=head
                    t2=head.next
                    head=head.next
                    break
                head=head.next
            x=self.reverse(head,d)

            #if left is not starting position but right is the ending of linked list
            if right==n:
                t1.next=x[0]
                return temp
            #if left and right both are not ends of the linked list
            else:
                t1.next=x[0]
                t2.next=x[1]
                return temp