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
        currentStr = ""
        #Build current string and add it to res

        def backtrack(i):
            nonlocal currentStr, res
            #Base Case: 
            #If we exhaused the index out of bounds of digits
            #That tells us that we added n values to the current combination
            if i == len(digits):
                #If the current string combiniation is not empty
                if currentStr:
                    #Stringify the current String

                    #Add it to res
                    res.append(currentStr)
                return
            
            #For each character in the current digit
            for char in digitsMap[digits[i]]:
                currentStr= currentStr + char
                #Add the character,
                #Traverse the decision tree in adding characters associated wth the next digit (i+1)
                #By Calling the backtrack function
                
                backtrack(i+1)
                
                #Once done, pop the currentString to try the next combination of digits
                #Starting with the next value of the first digit (next char in digitsMap[digits[i]])
                currentStr=currentStr[:i]
                  
        backtrack(0)
        return res 

