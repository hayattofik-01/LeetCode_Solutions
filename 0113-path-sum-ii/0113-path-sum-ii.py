# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def helper(node,sum_,path):
            
            if not node:
                return 
            path.append(node.val)
            if not node.left and not node.right and  sum_ + node.val  == targetSum:
                
                ans.append(path.copy())
            
            
                
            
            helper(node.left,sum_  + node.val,path)
            helper(node.right,sum_ + node.val,path)
            path.pop()
            
        helper(root,0,[])
        
        return ans 
        
            
        