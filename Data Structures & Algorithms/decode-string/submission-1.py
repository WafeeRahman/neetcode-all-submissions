class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []

        curStr = ''
        k=0
        for char in s:
            if char.isdigit():
                k *= 10
                k+=int(char)
            
            elif char == "[":
                countStack.append(k)
                stringStack.append(curStr)
                curStr = ''
                k=0
            
            elif char == ']':
                prevCount = countStack.pop()
                prevStr = stringStack.pop()
                curStr = prevStr + (curStr*prevCount)
            else:
                curStr += char
        return curStr

            
            