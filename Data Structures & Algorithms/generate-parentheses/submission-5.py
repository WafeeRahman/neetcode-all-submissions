class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(openC, closedC):
            nonlocal n
            #If there are n opens and n closed
            #This is a valid parenthesis, add the stack
            if openC == closedC == n:
                res.append(''.join(stack))
                return
            
            #If there arent n opens
            #Explore the decision of adding an open, afterwards
            #Pop to explore the decision of not adding an open
            if openC < n:
                stack.append("(")
                backtrack(openC+1, closedC)
                stack.pop()
         
            if closedC < openC:
                stack.append(")")
                backtrack(openC, closedC+1)
                stack.pop()
        
        backtrack(0, 0)
        return res

            



        