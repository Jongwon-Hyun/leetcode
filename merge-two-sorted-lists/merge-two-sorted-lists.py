# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = ListNode(-1)
        cursor = merged_head
        
        while list1 and list2:
            if list1.val > list2.val:
                cursor.next = list2
                list2 = list2.next
            else:
                cursor.next = list1
                list1 = list1.next
            
            cursor = cursor.next
        
        if list1:
            cursor.next = list1 
        else:
            cursor.next = list2
        
        return merged_head.next