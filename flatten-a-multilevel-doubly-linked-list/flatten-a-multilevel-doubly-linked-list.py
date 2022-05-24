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
        curr = head

        while curr:
          if curr.child:
            cachedNext = curr.next
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
            tail = curr.next
            while tail.next:
              tail = tail.next
            tail.next = cachedNext
            if cachedNext:
              cachedNext.prev = tail
          curr = curr.next

        return head