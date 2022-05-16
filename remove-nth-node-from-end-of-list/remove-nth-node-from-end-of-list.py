# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            head = None
            return head
            
        pointer1 = head
        pointer2 = head
        for _ in range(n):
            pointer2 = pointer2.next
        
        if pointer2 is None:
            head = head.next
            return head
            
        while pointer2.next is not None:
            pointer2 = pointer2.next
            pointer1 = pointer1.next
            
        pointer1.next = pointer1.next.next
        
        return head