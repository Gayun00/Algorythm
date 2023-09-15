from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        que = deque()
        que.append((root, 1))
        max_depth = 0
        
        while que:
            cur_node, cur_depth = que.popleft()
            max_depth = max(cur_depth, max_depth)
            
            if cur_node.left:
                que.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                que.append((cur_node.right, cur_depth + 1))
                
        return max_depth