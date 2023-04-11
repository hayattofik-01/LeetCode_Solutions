# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ans= []
        def dfs(root):
            if root == None:
                return 
            self.ans.append("(")
            self.ans.append(str(root.val))
            
           
            if not root.left and root.right:
                self.ans.append("()")
            dfs(root.left)
            dfs(root.right)
            self.ans.append(")")
            
            
           
        dfs(root)
        return "".join(self.ans)[1:-1]


        