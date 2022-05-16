# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer1 = headA
        pointer2 = headB
        
        while pointer1 != pointer2:
            pointer1 = headB if pointer1 is None else pointer1.next
            pointer2 = headA if pointer2 is None else pointer2.next
                
        return pointer1