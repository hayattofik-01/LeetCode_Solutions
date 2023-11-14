class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ope = []
        close = []
        
        for i in range(len(s)):
            if s[i] == "(":
                ope.append(i)
            elif ope and s[i] == ")":
                ope.pop()
            elif s[i] == ")":
                close.append(i)
        tobeRe  = ope + close
        tobeRe = set(tobeRe)
        ans = ['']
        for i in range(len(s)):
            if i in tobeRe:
                continue
            ans.append(s[i])
        return ''.join(ans)
    
            
        
        
        