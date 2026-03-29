class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #HashMap containing all Digits and possible associated values
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
        #Build 

        def backtrack(i):
            nonlocal currentStr, res
            #If our ith pointer is out of bounds, that tells us
            #We have exhausted the current string
            #And can return it to 
            if i == len(digits):
                if currentStr:
                    currentSTRcopy = ''.join(currentStr)
                    res.append(currentSTRcopy)
                return
            
            for char in digitsMap[digits[i]]:
                currentStr.append(char)
                backtrack(i+1)
                currentStr.pop()

            
        backtrack(0)
        return res 

