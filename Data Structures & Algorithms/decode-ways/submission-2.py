#Find all possible combinations that a string of integers that can be represented with their ascii counterparts
#Ex 1012 -> 10 1 2 -> J A B
    #or 10 12 JL
    #But not 1 01 2, because anything with zero infront isnt a valid ascii value
#At each step, we need to consider if we should consider the ith value as one valid digit, or conisder it and its
#Next digit as a valid letter
#If the current decoded part is >= 1  <= 26, then it is a valid part
#OTWS we cannot add the current value
#If we ever reach beyond the length of s, that tells us we completed a valid combination
class Solution:
    def numDecodings(self, s: str) -> int:
        res = []
        def dfs(i):
            if i >= len(s):
                return 1
            paths = 0
            if s[i] != "0":
                paths += dfs(i+1)
            
            if i < len(s)-1:
                if ((s[i] == "1" and (s[i+1] >= "0" and s[i+1] <= "9")) or 
                    (s[i] == "2" and  s[i+1] < "7")):
                    paths += dfs(i+2)
            return paths
        
        return dfs(0) 


            

        