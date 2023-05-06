# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS solution
        que = deque()  # we use first in first out quene for Breadth-First-search
        res = []
        que.append(root)
        
        while(que):   # loop through every level
            qlen = len(que)   # how many elements in the current row
            tmp = 0
            for i in range(qlen):   # loop through elements in current level
                node = que.popleft()
                tmp += node.val
                if node.left:   
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tmp/qlen)    # calculate the average 
        
        return res
      