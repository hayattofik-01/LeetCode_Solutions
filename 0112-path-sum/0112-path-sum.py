# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,Sum):
            if not root:
                return False
            Sum += root.val
            if not root.right and not root.left and Sum == targetSum:
                return True
            
            return dfs(root.left,Sum) or dfs(root.right,Sum)
            
        return dfs(root,0)
            
            
         
        