"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        values = []
        new_head = None
        tail = None

        def traverse(node):
            if node is None:
                return

            # Store the current node's value
            values.append(node.val)

            # Traverse the child list first
            if node.child is not None:
                traverse(node.child)

            # Continue with the next node
            node = node.next
            traverse(node)

        traverse(head)

        # Create a new flattened doubly linked list
        for value in values:
            new_node = Node(value)

            if new_head is None:
                new_head = new_node
                tail = new_node
            else:
                tail.next = new_node
                new_node.prev = tail
                tail = new_node

        return new_head