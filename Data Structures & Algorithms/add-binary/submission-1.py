class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        newStr = ""

        a = a[::-1]
        b = b[::-1]

        i = 0
        j = 0
        carry = "0"
        while i < len(a) or j < len(b) or carry:
            if i >= len(a) and j >= len(b) and carry == "0":
                break
            digitOne = a[i] if i <len(a) else "0"
            digitTwo = b[j] if j <len(b) else "0"
            digitSum = ""
            if digitOne == "1" and digitTwo == "1":
                if carry == "1":
                    digitSum = "1"
                    carry = "1"
                else:
                    carry = "1"
                    digitSum = "0"
            elif (digitOne=="1" or digitTwo == "1"):
                if carry == "1":
                    digitSum = "0"
                    carry = "1"
                else:
                    digitSum = "1"
            else:
                if carry == "1":
                    digitSum = "1"
                    carry = "0"
                else:
                    digitSum = "0"
            i+=1
            j+=1
            newStr += digitSum
        
        newStr = newStr[::-1]
        return newStr

                