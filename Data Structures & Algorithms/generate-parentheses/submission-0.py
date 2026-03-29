class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        #Create Recursive BackTracking Function

        def BackTrack(openCount, closeCount):
            #If the closed parenthesis count ever exceeds the open, the parenthesis are invalid
            #Ex ")", "()))", etc
            #Base Case for a Valid Parenthesis, if there are n opens with matching n closings
            if openCount == closeCount == n:
                res.append("".join(stack)) 
                return
            if openCount < n:
                stack.append("(")
                BackTrack(openCount+1, closeCount)
                stack.pop()
            if openCount < closeCount:
                stack.pop()
                return
            elif openCount > closeCount: 
                stack.append(")")
                BackTrack(openCount, closeCount+1)
                stack.pop()    
        BackTrack(0,0)
        return res

       
        