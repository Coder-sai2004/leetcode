# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head.next
        traverse_node = current_node.next

        while traverse_node.next:
            
            if traverse_node.val != 0:
                current_node.val += traverse_node.val
                traverse_node = traverse_node.next
                current_node.next = traverse_node
            else:
                current_node.next = traverse_node.next
                current_node = traverse_node.next
                traverse_node = current_node.next

        temp=head.next
        while temp.next.next:
            temp=temp.next
        temp.next=None

        return head.next