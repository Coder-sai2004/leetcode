# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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
        n=0
        dummy=head
        while dummy:
            n+=1
            dummy=dummy.next

        if head and head.next is None:
            return head

        d=right-left
        if left==1 and right==n:
            x=self.reverse(head,d)
            return x[0]

        elif left==1 and right!=n:
            t1=head
            x=self.reverse(head,d)
            t1.next=x[1]
            return x[0]

        elif left!=1:
            i=0
            temp=head
            while head:
                i+=1
                if i==left-1:
                    t1=head
                    t2=head.next
                    head=head.next
                    break
                head=head.next
            x=self.reverse(head,d)

            if right==n:
                t1.next=x[0]
                return temp
            else:
                t1.next=x[0]
                t2.next=x[1]
                return temp
        # else:
        #     i=0
        #     while head:
        #         i+=1
        #         if i==left-1:
        #             t1=head
        #             t2=head.next
        #             head=head.next
        #             break
        #         head=head.next
        #     x=self.reverse(head,d)