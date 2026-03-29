class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for token in operations:
            if token in "+DC":

                if token == "+":
                    opTwo = int(stack.pop())
                    opOne = int(stack.pop())

                    stack.append(opOne)
                    stack.append(opTwo)

                    stack.append(opOne + opTwo)
                    
                    
                
                elif token == "D":
                    opOne = stack.pop()
                    stack.append(int(opOne))
                    stack.append(int(opOne)*2)
                
                elif token == "C":
                    stack.pop()
            
            else:
                stack.append(token)
            print(stack)
        
        curSum = 0
        for i in range(len(stack)):
            curSum += int(stack[i]) 
        return curSum
            
        
        