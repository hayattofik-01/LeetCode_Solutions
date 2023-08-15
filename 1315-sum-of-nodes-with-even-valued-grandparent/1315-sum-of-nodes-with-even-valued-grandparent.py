# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        count  = 0 
        
        def dfs(parent,grand,cur):
            nonlocal count
            if not cur :
                return 
            if parent!= grand and grand.val % 2  == 0:
                count += cur.val
            dfs(cur,parent,cur.left)
            dfs(cur,parent,cur.right)
            return count 
        return dfs(root,root,root)
        
       
            
        