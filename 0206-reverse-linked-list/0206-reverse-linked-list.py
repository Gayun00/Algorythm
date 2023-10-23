# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(head, next_node):
            if next_node is None:
                return head
            temp = next_node.next
            next_node.next = head
            
            return dfs(next_node, temp)
         
        return dfs(None, head)
        
