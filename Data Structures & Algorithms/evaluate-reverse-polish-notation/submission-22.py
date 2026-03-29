class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if not token in "+*-/":
                stack.append(token)
            else:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                print(val1, val2)
                if token == "+":
                    stack.append(val1+val2)
                elif token == "*":
                    stack.append(val1*val2)
                elif token == "/":
                    stack.append(val1/val2)
                elif token == "-":
                    stack.append(val1 - val2)
        return int(stack[-1])
                    
        