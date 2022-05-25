"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        cursor = head
        while cursor:
            new_node = Node(cursor.val,cursor.next)
            cursor.next = new_node
            cursor = new_node.next
        
        cursor = head
        copy = head.next
        while cursor:
            if cursor.next:
                cursor.next.random = cursor.random.next if cursor.random else None
            cursor = cursor.next.next
        
        cursor = head
        while cursor and cursor.next:
            cursor.next,cursor = cursor.next.next,cursor.next

        return copy