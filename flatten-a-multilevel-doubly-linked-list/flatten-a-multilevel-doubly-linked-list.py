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
        cursor = head
        
        while cursor:
            if cursor.child:
                will_next = cursor.next
                cursor.next = cursor.child
                cursor.child.prev = cursor
                cursor.child = None
                tail = cursor.next
                while tail.next:
                    tail = tail.next
                tail.next = will_next
                if will_next:
                    will_next.prev = tail
            
            cursor = cursor.next
        
        return head