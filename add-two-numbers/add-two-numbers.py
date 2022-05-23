# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = ListNode(0)
        cursor = sum_head
        up = 0
        while l1 and l2:
            sum_val = up + l1.val + l2.val
            up = sum_val // 10
            digit = sum_val % 10
            
            cursor.next = ListNode(digit)
            cursor = cursor.next
            l1,l2 = l1.next,l2.next
        
        if l1:
            while l1:
                sum_val = up + l1.val
                up = sum_val // 10
                digit = sum_val % 10
                
                cursor.next = ListNode(digit)
                cursor = cursor.next
                l1 = l1.next
        elif l2:
            while l2:
                sum_val = up + l2.val
                up = sum_val // 10
                digit = sum_val % 10
                
                cursor.next = ListNode(digit)
                cursor = cursor.next
                l2 = l2.next
        
        if up:
            cursor.next = ListNode(up)
        
        return sum_head.next