# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=None
        tail=None
        while list1 and list2:
            if list1.val<=list2.val:
                node=list1
                list1=list1.next
                node.next=None
                if head is None:
                    head=node
                    tail=node
                else:
                    tail.next=node
                    tail=node
            elif list2.val<list1.val:
                node=list2
                list2=list2.next
                node.next=None
                if head is None:
                    head=node
                    tail=node
                else:
                    tail.next=node
                    tail=node
        
        if list1:
            if head is None:
                head=list1
                tail=list1
            else:
                tail.next=list1
        if list2:
            if head is None:
                head=list2
                tail=list2
            else:
                tail.next=list2
        
        return head