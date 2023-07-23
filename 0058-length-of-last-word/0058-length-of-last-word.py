class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        val = s.split(" ")
     
        for i in range(len(val)-1,-1,-1):
            if val[i] != '':
                return len(val[i])
        