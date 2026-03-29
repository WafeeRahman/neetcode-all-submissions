class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketDict = {")":"(", "]":"[", "}":"{"}
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif s[i] in ")]}":
                if not (stack):
                    return False 
                if stack[-1] == bracketDict[s[i]]:
                    stack.pop()
                else:
                    return False
        return not stack
        