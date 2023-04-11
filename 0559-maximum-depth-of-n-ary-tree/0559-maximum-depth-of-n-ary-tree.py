"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        
        def dfs(root):
            if not root:
                return 0
            elif root.children:
                return max( self.maxDepth(child) for child in root.children ) + 1
            else:
                return 1
        return dfs(root) 
           
            
                
           
        
        
        
        
        