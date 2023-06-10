class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        end=len(needle)
        for start in range(len(haystack)):
            if haystack[start:end]==needle:
                return start
            end+=1
        return -1 
        