class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for l in s:
            if stack and stack[-1][0] == l:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
                    
            else:
                stack.append([l,1])
                
        ans = [""]
        for v in stack:
            for i in range(v[1]):
                ans.append(v[0])
        return "".join(ans)
            
        
        