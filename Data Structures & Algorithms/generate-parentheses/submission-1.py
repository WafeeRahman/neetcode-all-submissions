class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        #Create Recursive BackTracking Function
        #Find Valid Parenthesis, BackTrack

        def BackTrack(openCount, closeCount):
            #If the closed parenthesis count ever exceeds the open, the parenthesis are invalid
            #Ex ")", "()))", etc
            #Base Case for a Valid Parenthesis, if there are n opens with matching n closings
            
            if openCount == closeCount == n:
                res.append("".join(stack)) #Append the String Built in the Stack
                return #Break out of Recursion
            
            if openCount < n:
                stack.append("(")
                BackTrack(openCount+1, closeCount)
                stack.pop() #BackTrack after finding or not finding a valid path
            
            if openCount < closeCount:
                stack.pop() #If we find a invalid parenthnesis, pop the stack
                return # Return
            
            #We are only to add a closing when opens > closing
            if openCount > closeCount: 
                stack.append(")") 
                BackTrack(openCount, closeCount+1) #Run algo to find valid path
                stack.pop() #Backtrack after pathing

        BackTrack(0,0)
        return res

       
        