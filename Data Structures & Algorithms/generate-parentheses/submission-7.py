class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []
        def generateParens(openCount, closeCount):
            
            if openCount == closeCount == n:
                res.append(''.join(stack))
                return
            
            if closeCount > openCount:
                return
            
            if openCount < n:
                stack.append("(")
                generateParens(openCount+1, closeCount)
                stack.pop()
                
            if closeCount < openCount:
                stack.append(")")
                generateParens(openCount, closeCount+1)
                stack.pop()
       
        generateParens(0,0)
        return res