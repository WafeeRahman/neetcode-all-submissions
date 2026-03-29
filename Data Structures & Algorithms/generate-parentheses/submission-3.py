class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack= []
        res = []

        def backtrack (openCount, closeCount):

            if openCount == closeCount == n:
                res.append("".join(stack))
                
                return

            if openCount < n:
                stack.append("(")
                backtrack(openCount+1, closeCount)
                stack.pop()    
            if openCount > closeCount:
                stack.append(")")
                backtrack(openCount, closeCount+1)
                stack.pop()
        backtrack(0,0)
        return res

