# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        
        first = head
        cur = head.next
        
        while cur:
            head.next = cur.next
            tmp = cur.next
            cur.next = first
            first, cur = cur, tmp            
            
        return first