class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opsStack = []

        for token in tokens:
            if not token in "+-*/":
                opsStack.append(token)
            else:
                opTwo = int(opsStack.pop())
                opOne = int(opsStack.pop())
                if token == "+":
                    opsStack.append(opOne + opTwo)
                elif token == "-":
                    opsStack.append(opOne - opTwo)

                elif token == "*":
                    opsStack.append(opOne * opTwo)

                elif token == "/":
                    opsStack.append(opOne/opTwo)
        
        return int(opsStack[-1])
            
