# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = dummy = ListNode(-1)
        carry = 0
        
        while l1 and l2:
            carry, digit = divmod(l1.val + l2.val + carry, 10)
            node.next = ListNode(digit)
            l1, l2, node = l1.next, l2.next, node.next
            
        l = l1 or l2
        while l:
            carry, digit = divmod(l.val + carry, 10)
            node.next = ListNode(digit)
            l, node = l.next, node.next
        if carry:
            node.next = ListNode(carry)
        
        return dummy.next
            
        