# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode(-1)
        carry = 0
        
        while l1 and l2:
            carry, digit = divmod(l1.val + l2.val + carry, 10)
            head.next = ListNode(val= digit)
            head = head.next
            l1,l2 = l1.next, l2.next
            
        l = l1 or l2
        while l:
            carry, digit = divmod(l.val + carry, 10)
            head.next = ListNode(val = digit)
            head = head.next
            l=l.next
            
        if carry:
            head.next=  ListNode(val=carry)
            
        return dummy.next