# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current = list1
        index = 0
        prev = None
        next_node = None

        while current:
            if index == a - 1:
                prev = current
            if index == b + 1:
                next_node = current

            current = current.next
            index += 1

        prev.next = list2

        while list2.next:
            list2 = list2.next

        list2.next = next_node

        return list1