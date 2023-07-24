# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def maxPathSumHelper(node):
            if not node:
                return 0
            left_sum = max(0, maxPathSumHelper(node.left))
            right_sum = max(0, maxPathSumHelper(node.right))
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
            return node.val + max(left_sum, right_sum)
        
        maxPathSumHelper(root)
        return self.max_sum
        
        
        
        
        