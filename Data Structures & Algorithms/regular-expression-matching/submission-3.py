class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        memoC = {}

        def memo(i,j):
            #If we complete both the string and the pattern, that tells us we completed the string
            if i >= len(s) and j >= len(p):
                return True
            #If we dont complete the string but complete the patter invalid
            if j >= len(p):
                return False
            if (i,j) in memoC:
                return memoC[(i,j)]
            
            #If we are in bounds of s, and have match between characters, or a . pattern we can match the current chracter
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            #If there is a glob pattern, we need to make decisions of repeated curchar vs not
            #To avoid indexing error check if (j+1) < len(p) 
            if (j+1) < len(p) and p[j+1] == "*":
                #If there is a pattern we need to make two choices
                #To not repeat the character and move to the next value (j+2)
                #Or repeat the character, first we need to check if there's a match
                memoC[(i,j)] = memo(i, j+2) or (match and memo(i+1, j))
                return memoC[(i,j)]
            
            if match:
                memoC[(i,j)] = memo(i+1,j+1)
                return memoC[(i,j)]
            
            else:
                memoC[(i,j)] = False
                return memoC[(i,j)]
        
        return memo(0,0)
