class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ref = {"2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs", "8" :"tuv", "9":"wxyz"
              }
        ans = [""]
        
        for num in digits:
            combination = []
            for a in ans :
                for letter in ref[num]:
                    combination.append( a + letter)
            ans = combination
        return ans
        