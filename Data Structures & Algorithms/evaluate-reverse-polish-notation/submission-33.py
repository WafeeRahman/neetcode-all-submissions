class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        opStack = []
        for token in tokens:
            if not token in "*/+-":
                opStack.append(int(token))

            if token in "*/+-":
                opTwo = opStack.pop()
                opOne = opStack.pop()
                print(opStack, opOne, opTwo, token)
                if token == "*":
                    opStack.append(opOne * opTwo)
                elif token == "/":
                    opStack.append(int(opOne/opTwo))
                elif token == "+":
                    opStack.append(opOne + opTwo)
                elif token == "-":
                    opStack.append(opOne - opTwo)

        return opStack[-1]