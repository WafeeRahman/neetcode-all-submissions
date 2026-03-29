class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {"(":")", "{":"}", "[":"]"}
        stack = []
        for paren in s:
            if paren in "({[":
                stack.append(paren)
            else:
                if not stack or bracketMap[stack[-1]] != paren:
                    return False
                stack.pop()
        return stack == []


        