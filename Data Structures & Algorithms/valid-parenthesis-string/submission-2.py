#Given a string s that can only consist of () or *, return true if s is a valid parenthesis
#A string is a valid if every ( has a matching ), every ) has a matchign (, and every ( is before its corresponding )
#A * can be a left or right, or treated as empty

#S = Input: s = "((**)", One of the * can be treated as a ) to match the open parens
#Input: s = "(((*)"
class Solution:
    def checkValidString(self, s: str) -> bool:
        #Keep track of a count for opens, and the maximum amount of opens we can have considering turning * into
        #(, decrement the opencount each time we encounter a )
        curOpen, maxOpen = 0, 0

        for i in range(len(s)):
            if s[i] == "(":
                curOpen += 1
                maxOpen += 1
            
            if s[i] == "*":
                maxOpen += 1
                curOpen -= 1
                curOpen = max(curOpen, 0)
            
            if s[i] == ")":
                curOpen -= 1
                maxOpen -= 1

            if maxOpen < 0:
                return False
            if curOpen < 0:
                curOpen = 0
        return curOpen == 0





        
        