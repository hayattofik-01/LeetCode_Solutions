class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        m=""        
        def helper1(i):
            nonlocal m
            l=i
            r=i
            while(0<=l and r<n and s[l]==s[r]):
                if(len(m)<r-l+1):
                    m=s[l:r+1]
                l=l-1
                r=r+1
            return
        def helper2(i):
            nonlocal m
            l=i
            r=i+1
            while(0<=l and r<n and s[l]==s[r]):
                if(len(m)<r-l+1):
                    m=s[l:r+1]
                l=l-1
                r=r+1
            return

        for i in range(0,len(s)):
            helper1(i)
            helper2(i)
        return m