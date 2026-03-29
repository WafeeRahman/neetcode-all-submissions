class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = 0
        stack = []

        for token in tokens:
            if token not in "*-+/":
                stack.append(token)
                print(token)
            
            else:
                operandTwo = int(stack.pop())
                operandOne = int(stack.pop())
                if token == "*":
                    stack.append(operandOne * operandTwo)
                elif token == "+":
                    stack.append(operandOne + operandTwo)
                elif token == "-":
                    stack.append(operandOne - operandTwo)
                elif token == "/":
                    stack.append(operandOne / operandTwo)
            print(stack)

        return int(stack[-1])

        