# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        rowcol = defaultdict(list)
        maxCol = 0
        def traverse(root,rc,level):
            nonlocal maxCol
            if not root:
                return 
          
            maxCol = max(maxCol, rc[1])
            rowcol[rc[1]].append((level,root.val))
            traverse(root.left, (rc[0] + 1,rc[1] - 1),level + 1)
           
            traverse(root.right, (rc[0] + 1,rc[1] + 1),level + 1)
            
        traverse(root,(0,0),0)
        output = []
    
        for key in sorted(rowcol.keys()):
            cur = []
            rowcol[key].sort()
            for val in rowcol[key]:
                cur.append(val[1])
            output.append(cur)
        return output
            
        