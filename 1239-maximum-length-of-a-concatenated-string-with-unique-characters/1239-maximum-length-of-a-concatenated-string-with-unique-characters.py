class Solution:
    def maxLength(self, arr: List[str]) -> int:
        visited = set()
        
        def notRepeated(array):
            
            prev =set()
            
            for i in range(len(array)):
                
                if array[i] in prev or array[i] in visited:
                    return False
                prev.add(array[i])
            return True
        
        def backTrack(i):
            
            if i == len(arr):
                return len(visited)
            
            res = 0 
            
            if notRepeated(arr[i]):
                for l in arr[i]:
                    visited.add(l)
                    
                res = backTrack(i+1)
                for l in arr[i]:
                    visited.remove(l)
            return max(res,backTrack(i+1))
        return backTrack(0)
            
                    
                
       
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#             cnt += 1
            
#             if i > len(lis):
#                 return 
            
#             for i in range(cur,len(arr)):
                
#                 for  i 
        
#         for i in range(len(arr)):
#             visited = set()
#             dupl = False
#             for j in arr[i]:
#                 if j in visited:
#                     dupl = True
#                     break
#                 visited.add(j)
            
#             if not dupl:
#                 backTrack(i+1, cnt)
            
            
                
                
#         return 9
            
            
            
            