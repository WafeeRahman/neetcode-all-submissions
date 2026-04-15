class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digitMap = {"1":"",
         "2": "abc",
         "3":"def",
         "4":"ghi",
         "5":"jkl",
         "6":"mno",
         "7":"pqrs",
         "8": "tuv",
         "9": "wxyz"}
        res = []
        curStr = []
        def genCombinations(i):
            if i >= len(digits):
                res.append(''.join(curStr))
                return 
            
            for j in range(len(digits[i])):
                for char in digitMap[digits[i]]:
                    curStr.append(char)
                    genCombinations(i+1)
                    curStr.pop()
        genCombinations(0)
        return res
           

