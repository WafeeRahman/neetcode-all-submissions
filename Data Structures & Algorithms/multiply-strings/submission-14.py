#Guveb two strings num1 and num2, that are non negative integers
#represented as strings, return the product of them without converting the entire inputs to integers
#(digit by digit)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #If we arent converting the entire inputs into integers and multiplying them, then we have to do
        #Manual multiplications, starting from the rightmost digit and using carry's

        #We can start by converting each input value into their respective digit
        if "0" in [num1, num2]:
            return "0"

        digitsOne = [int(i) for i in num1][::-1]
        digitsTwo = [int(i) for i in num2][::-1]
        minLen = min(len(digitsOne), len(digitsTwo))
        #Any two numbers multiplied can only be as long as the two digits combined
        res = [0] * (len(digitsOne) + len(digitsTwo))
        carry = 0
        
        #Multiply each value in digits two byt 
        for i in range(len(digitsOne)):
            for j in range(len(digitsTwo)):
                #Multiply each number from digit two to digit one like in traditional mult
                product = digitsTwo[j] * digitsOne[i]
                res[i+j] += product
                res[i + j+1] += res[i+j] // 10 #Carry Over
                res[i+j] = res[i+j] % 10 #Set the first digit, and carry the next value
        
        res.reverse()
        beginning = 0
        #Find the first digit
        while beginning < len(res) and res[beginning] == 0:
            beginning += 1
        retnSTR = ""

        for i in range(beginning, len(res)):
            retnSTR += str(res[i])
        return retnSTR



        






        
            
        