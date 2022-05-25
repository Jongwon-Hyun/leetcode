# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        if k == 0 or not head.next:
            return head

        cursor = head
        last_node = None
        len = 0
        while cursor:
            len += 1
            if not cursor.next:
                last_node = cursor
            cursor = cursor.next
            
        k = k % len
        if k == 0: 
            return head

        target_node = head         
        for _ in range(len - k - 1):
            target_node = target_node.next
        
        last_node.next,head,target_node.next = head,target_node.next,None 
        
        return head