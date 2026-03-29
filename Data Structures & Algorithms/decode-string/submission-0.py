class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        letterStack = []
        k = 0
        curStr = ""
        for char in s:
            
            #Scan Digits for k[encoded string]
            if char.isdigit():
                k = k*10
                k += int(char)
            elif char == "[":

                countStack.append(k)
                letterStack.append(curStr)
                print(countStack, letterStack)
                curStr = ""
                k=0
            elif char == "]":
                print(countStack, letterStack)
                prevCount = countStack.pop()
                prevStr = letterStack.pop()
                curStr = prevStr + curStr*prevCount
                
            else:
                curStr += char
        return curStr


        