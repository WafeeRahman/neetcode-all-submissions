class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketMappings = {")":"(", "]":"[", "}":"{" }
        stack = []

        for char in s:
            if char in ")]}":
                if stack and stack[-1] == bracketMappings[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0