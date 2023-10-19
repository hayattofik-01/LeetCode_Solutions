# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = defaultdict(int)
        ans = []
        
        def preOrder(root):
            
            if not root:
                return ""
            
            left = preOrder(root.left)
            right = preOrder(root.right)
            
            id_ = f"({left})" + (str(root.val)) + f"({right})"
            count[id_] +=1
            
            if count[id_] == 2 :
                ans.append(root)
            
                
                
            return id_
        preOrder(root)

        return set(ans)
                
            
            
        
       