class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token in "+-*/":
                opTwo = int(stack.pop())
                opOne = int(stack.pop())
                if token == "+":
                    stack.append(opOne + opTwo)
                elif token == "-":
                    stack.append(opOne - opTwo)
                elif token == "/":
                    stack.append(int(opOne/opTwo))
                elif token == "*":
                    stack.append(opOne*opTwo)

            else:
                stack.append(token)
        return int(stack[-1])