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
            sum_ += node.val
            path.append(node.val)
            if not node.left and not node.right and sum_== targetSum:

                ans.append(path.copy())
                
            
            helper(node.left,sum_,path)
            
            helper(node.right,sum_,path)
            path.pop()
            
            
            
            
        helper(root,0,[])
        
        return ans 
        
            
        