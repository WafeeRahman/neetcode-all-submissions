class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        total = 0
        carry = 0
        i = 0
        j = 0

        a = a[::-1]
        b = b[::-1]
        res = ""

        while i < len(a) or j < len(b) or carry:
            total = carry
            carry = 0
            if i < len(a):
                total += int(a[i])
                i+=1
            
            if j < len(b):
                total += int(b[j])
                j+=1
            res += str(total % 2)
            carry = total // 2

        return res[::-1]