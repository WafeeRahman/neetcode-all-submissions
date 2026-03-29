class Solution:
    def multiply(self, num1: str, num2: str) -> str:
     

        minLen = min(len(num1), len(num2))
        newS = ""
        baseOne = len(num1)-1
        val1 = 0
        for i in range(len(num1)):
            digitOne = (ord(num1[i]) - ord('0'))
            val1 += digitOne * (10**baseOne)
            baseOne -= 1
        
        baseOne = len(num2)-1
        val2 = 0
        for i in range(len(num2)):
            digitOne = (ord(num2[i]) - ord('0'))
            val2 += digitOne * (10**baseOne)
            baseOne -= 1
        
        return str(val1*val2)
            
        