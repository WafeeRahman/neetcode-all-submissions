class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = { "[": "]", "(":")", "{": "}"}
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")]}":
                if len(stack) == 0:
                    return False
                bracketType = stack.pop()
                #If the most recent open bracket doesnt match the type
                #of the close bracket, the parentheses is invalid
                if char != bracketMap[bracketType]:
                    return False
        return len(stack) == 0