class Solution:
    def isValid(self, brackets: str) -> bool:
        match = {')':'(' , '}':'{',']':'['}
        seenBrackets = []
        openRef = {'(', '{','['}

        for bracket in brackets:
            if bracket in openRef:
                seenBrackets.append(bracket)
            else:
                expectedMatch = "not found"
                if seenBrackets:
                    expectedMatch = seenBrackets.pop()
                if not match[bracket] == expectedMatch:
                    return False
        if not seenBrackets:
            return True
        return False
