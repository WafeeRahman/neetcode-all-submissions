class Solution:
    def isValid(self, s: str) -> bool:
        brackMap = {"]":"[", "}":"{", ")":"("}
        stack = []

        for value in s:
            if value in ")]}":
                if not stack or stack[-1] != brackMap[value]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(value)
        return not stack

        