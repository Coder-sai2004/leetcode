# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        # Store target values for quick lookup
        values = set(nums)
        count = 0
        found = False

        # Traverse the linked list
        while head:
            if head.val in values:
                found = True
            elif found:
                count += 1
                found = False

            head = head.next

        # Count the last component if it exists
        if found:
            count += 1

        return count