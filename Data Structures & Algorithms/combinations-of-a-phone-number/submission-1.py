class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        res = []
        currentStr = []

        def backtrack(i):
            nonlocal currentStr, res
            if i == len(digits):
                currentSTRcopy = ''.join(currentStr)
                res.append(currentSTRcopy)
                return
            
            for char in digitsMap[digits[i]]:
                currentStr.append( char)
                backtrack(i+1)
                currentStr.pop()

            
        backtrack(0)
        return res if res != [""] else []

