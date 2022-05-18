# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        
        i = 2
        prev = head
        cur = head.next
        last_odd = head
        while cur:
            if i % 2 == 0:
                prev, cur = cur, cur.next
            else:
                prev.next, cur.next, last_odd.next, last_odd, cur = cur.next, last_odd.next, cur, cur, cur.next
            
            i += 1
        
        return head