class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = defaultdict(int)
        for l in magazine:
            dic[l] +=1
        for l in ransomNote:
            if dic[l] >=1:
                dic[l] -=1
            else:
                return False
        return True
        