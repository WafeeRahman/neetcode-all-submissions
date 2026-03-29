class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(openC, closedC):
            nonlocal n
            if openC == closedC == n:
                res.append(''.join(stack))
                return
            
            if openC < n:
                stack.append("(")
                backtrack(openC+1, closedC)
                stack.pop()
            
            if closedC > openC:
                return 
            
            if closedC < openC:
                stack.append(")")
                backtrack(openC, closedC+1)
                stack.pop()
        
        backtrack(0, 0)
        return res

            



        