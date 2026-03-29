class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {')':'(','}':'{', ']':'['}
        stack = []


        for paren in s:
            if paren in "([{":
                stack.append(paren)
            else:
                if not stack:
                    return False
                elif stack and bracketMap[paren] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack